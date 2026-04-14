import json
import unittest

from package_sorter import create_app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    # ── Successful dispatches ───────────────────────────────────
    def test_standard_package(self):
        res = self.client.post("/api/sort", json={
            "width": 10, "height": 10, "length": 10, "mass": 5,
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["stack"], "STANDARD")
        self.assertEqual(data["volume"], 1000)

    def test_special_package(self):
        res = self.client.post("/api/sort", json={
            "width": 200, "height": 200, "length": 200, "mass": 10,
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["stack"], "SPECIAL")

    def test_rejected_package(self):
        res = self.client.post("/api/sort", json={
            "width": 150, "height": 150, "length": 150, "mass": 25,
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["stack"], "REJECTED")

    # ── Custom benchmarks ───────────────────────────────────────
    def test_custom_benchmarks(self):
        res = self.client.post("/api/sort", json={
            "width": 10, "height": 10, "length": 10, "mass": 5,
            "benchmarks": {"volume": 500, "dim": 5, "mass": 3},
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["stack"], "REJECTED")

    # ── Validation errors ───────────────────────────────────────
    def test_missing_fields(self):
        res = self.client.post("/api/sort", json={"width": 10})
        self.assertEqual(res.status_code, 400)

    def test_invalid_json(self):
        res = self.client.post(
            "/api/sort",
            data="not json",
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 400)

    def test_negative_dimensions(self):
        res = self.client.post("/api/sort", json={
            "width": -1, "height": 10, "length": 10, "mass": 5,
        })
        self.assertEqual(res.status_code, 400)

    def test_invalid_benchmark_values(self):
        res = self.client.post("/api/sort", json={
            "width": 10, "height": 10, "length": 10, "mass": 5,
            "benchmarks": {"volume": "abc", "dim": 5, "mass": 3},
        })
        self.assertEqual(res.status_code, 400)

    # ── Index page ──────────────────────────────────────────────
    def test_index_returns_html(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Package Sorter", res.data)


if __name__ == "__main__":
    unittest.main()
