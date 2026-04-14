from flask import Blueprint, request, jsonify, render_template

from .sort import sort, sort_with_benchmarks

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/api/sort", methods=["POST"])
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

    benchmarks = data.get("benchmarks")
    if benchmarks:
        try:
            result = sort_with_benchmarks(
                width, height, length, mass,
                volume_threshold=float(benchmarks["volume"]),
                dim_threshold=float(benchmarks["dim"]),
                mass_threshold=float(benchmarks["mass"]),
            )
        except (KeyError, TypeError, ValueError):
            return jsonify({"error": "Invalid benchmark values"}), 400
    else:
        result = sort(width, height, length, mass)

    return jsonify({
        "stack": result,
        "volume": width * height * length,
        "mass": mass,
    })
