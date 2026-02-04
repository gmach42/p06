def validate_ingredients(ingredients: str) -> str:
    """Validate a space-separated list of alchemical ingredients."""
    if all(
        ing in ["fire", "water", "earth", "air"]
        for ing in ingredients.split(" ")
    ):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
