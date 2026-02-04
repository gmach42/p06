def circular_curse_breaking() -> None:
    """Demonstrates breaking circular dependencies using late imports."""

    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    try:
        from alchemy.grimoire import record_spell, validate_ingredients

        ingredients1 = "fire air"
        ingredients2 = "dragon scales"

        result1 = validate_ingredients(ingredients1)
        result2 = validate_ingredients(ingredients2)
        print(f'validate_ingredients("{ingredients1}"): {result1}')
        print(f'validate_ingredients("{ingredients2}"): {result2}')
    except AttributeError as e:
        print(f"AttributeError: {e}")

    print("\nTesting spell recording with validation:")
    try:
        spell_name = "Fireball"
        ingredients = "fire air"
        spell_result = record_spell(spell_name, ingredients)
        print(f'record_spell("{spell_name}", "{ingredients}"): ', end="")
        print(spell_result)
    except AttributeError as e:
        print(f"AttributeError: {e}")

    try:
        spell_name = "Dark Magic"
        ingredients = "shadow"
        spell_result = record_spell(spell_name, ingredients)
        print(f'record_spell("{spell_name}", "{ingredients}"): ', end="")
        print(spell_result)
    except AttributeError as e:
        print(f"AttributeError: {e}")

    print("\nTesting late import technique:")
    try:
        from alchemy.grimoire.spellbook import record_spell

        spell_name = "Lightning"
        ingredients = "air"
        print(f'record_spell("{spell_name}", "{ingredients}"): ', end="")
        spell_result = record_spell(spell_name, ingredients)
        print(spell_result)
    except AttributeError as e:
        print(f"AttributeError: {e}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    circular_curse_breaking()
