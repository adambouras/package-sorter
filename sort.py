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
    volume = width * height * length
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
