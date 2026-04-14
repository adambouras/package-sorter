import unittest
from sort import sort


class TestSort(unittest.TestCase):
    # ── STANDARD: not bulky, not heavy ──────────────────────────
    def test_small_light_package(self):
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")

    def test_just_under_bulky_volume(self):
        # 99 * 99 * 99 = 970_299 < 1_000_000
        self.assertEqual(sort(99, 99, 99, 19), "STANDARD")

    def test_just_under_bulky_dimension(self):
        self.assertEqual(sort(149, 1, 1, 1), "STANDARD")

    # ── SPECIAL: bulky only ─────────────────────────────────────
    def test_bulky_by_volume(self):
        # 100 * 100 * 100 = 1_000_000
        self.assertEqual(sort(100, 100, 100, 19), "SPECIAL")

    def test_bulky_by_single_dimension(self):
        self.assertEqual(sort(150, 1, 1, 1), "SPECIAL")

    def test_bulky_by_height(self):
        self.assertEqual(sort(1, 150, 1, 5), "SPECIAL")

    def test_bulky_by_length(self):
        self.assertEqual(sort(1, 1, 150, 5), "SPECIAL")

    def test_bulky_volume_over_threshold(self):
        self.assertEqual(sort(200, 200, 200, 10), "SPECIAL")

    # ── SPECIAL: heavy only ─────────────────────────────────────
    def test_heavy_small_package(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    def test_heavy_above_threshold(self):
        self.assertEqual(sort(1, 1, 1, 100), "SPECIAL")

    # ── REJECTED: bulky AND heavy ───────────────────────────────
    def test_rejected_bulky_volume_and_heavy(self):
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")

    def test_rejected_bulky_dimension_and_heavy(self):
        self.assertEqual(sort(150, 1, 1, 20), "REJECTED")

    def test_rejected_both_bulky_criteria_and_heavy(self):
        self.assertEqual(sort(200, 200, 200, 50), "REJECTED")

    # ── Edge cases ──────────────────────────────────────────────
    def test_zero_dimensions(self):
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")

    def test_exact_volume_boundary(self):
        # exactly 1_000_000 → bulky
        self.assertEqual(sort(100, 100, 100, 0), "SPECIAL")

    def test_exact_dimension_boundary(self):
        self.assertEqual(sort(150, 1, 1, 0), "SPECIAL")

    def test_exact_mass_boundary(self):
        self.assertEqual(sort(1, 1, 1, 20), "SPECIAL")

    def test_all_at_boundary(self):
        self.assertEqual(sort(150, 100, 100, 20), "REJECTED")

    def test_fractional_values(self):
        self.assertEqual(sort(10.5, 10.5, 10.5, 19.9), "STANDARD")

    def test_very_large_package(self):
        self.assertEqual(sort(1000, 1000, 1000, 1000), "REJECTED")


if __name__ == "__main__":
    unittest.main()
