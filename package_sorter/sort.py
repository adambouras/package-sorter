"""Core sorting logic for the robotic arm dispatch system."""

# Default thresholds
DEFAULT_VOLUME_THRESHOLD = 1_000_000  # cm³
DEFAULT_DIM_THRESHOLD = 150           # cm
DEFAULT_MASS_THRESHOLD = 20           # kg


def sort(width: float, height: float, length: float, mass: float) -> str:
    """Dispatch a package to the correct stack based on its dimensions and mass.

    Args:
        width:  Width in centimeters.
        height: Height in centimeters.
        length: Length in centimeters.
        mass:   Mass in kilograms.

    Returns:
        "STANDARD", "SPECIAL", or "REJECTED".
    """
    return sort_with_benchmarks(
        width, height, length, mass,
        volume_threshold=DEFAULT_VOLUME_THRESHOLD,
        dim_threshold=DEFAULT_DIM_THRESHOLD,
        mass_threshold=DEFAULT_MASS_THRESHOLD,
    )


def sort_with_benchmarks(
    width: float,
    height: float,
    length: float,
    mass: float,
    *,
    volume_threshold: float = DEFAULT_VOLUME_THRESHOLD,
    dim_threshold: float = DEFAULT_DIM_THRESHOLD,
    mass_threshold: float = DEFAULT_MASS_THRESHOLD,
) -> str:
    """Dispatch a package using custom benchmark thresholds.

    Args:
        width:            Width in centimeters.
        height:           Height in centimeters.
        length:           Length in centimeters.
        mass:             Mass in kilograms.
        volume_threshold: Volume at which a package is considered bulky (cm³).
        dim_threshold:    Single-dimension limit for bulky classification (cm).
        mass_threshold:   Mass at which a package is considered heavy (kg).

    Returns:
        "STANDARD", "SPECIAL", or "REJECTED".
    """
    volume = width * height * length
    bulky = volume >= volume_threshold or max(width, height, length) >= dim_threshold
    heavy = mass >= mass_threshold

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
