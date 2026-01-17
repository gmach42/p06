def validate_ingredients(ingredients: str) -> str:
    if all(
        ing in ["fire", "water", "earth", "air"]
        for ing in ingredients.split(",")
    ):
        return f"[{ingredients}] - VALID"
    else:
        return f"[{ingredients}] - INVALID"
