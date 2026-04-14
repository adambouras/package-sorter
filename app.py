from flask import Flask, request, jsonify, send_from_directory
from sort import sort

app = Flask(__name__, static_folder=".", static_url_path="")


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/api/sort", methods=["POST"])
def sort_package():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    try:
        width = float(data["width"])
        height = float(data["height"])
        length = float(data["length"])
        mass = float(data["mass"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Provide numeric width, height, length, mass"}), 400

    if any(v < 0 for v in (width, height, length, mass)):
        return jsonify({"error": "Dimensions and mass must be non-negative"}), 400

    # Optional custom benchmarks from the frontend
    benchmarks = data.get("benchmarks")
    if benchmarks:
        try:
            bench_volume = float(benchmarks["volume"])
            bench_dim = float(benchmarks["dim"])
            bench_mass = float(benchmarks["mass"])
        except (KeyError, TypeError, ValueError):
            return jsonify({"error": "Invalid benchmark values"}), 400

        volume = width * height * length
        bulky = volume >= bench_volume or max(width, height, length) >= bench_dim
        heavy = mass >= bench_mass

        if bulky and heavy:
            result = "REJECTED"
        elif bulky or heavy:
            result = "SPECIAL"
        else:
            result = "STANDARD"
    else:
        result = sort(width, height, length, mass)

    volume = width * height * length
    return jsonify({
        "stack": result,
        "volume": volume,
        "mass": mass,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
