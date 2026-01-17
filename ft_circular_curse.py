def circular_curse_breaking():
    print("=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    try:
        from alchemy.grimoire import record_spell, validate_ingredients

        ingredients1 = "fire,water,earth"
        ingredients2 = "fire,water,lightning"

        print(f"Validating ingredients: {ingredients1}")
        result1 = validate_ingredients(ingredients1)
        print("Result:", result1)

        print(f"\nRecording spell with ingredients: {ingredients1}")
        spell_result1 = record_spell("Elemental Shield", ingredients1)
        print("Spell Result:", spell_result1)

        print(f"\nValidating ingredients: {ingredients2}")
        result2 = validate_ingredients(ingredients2)
        print("Result:", result2)

        print(f"\nRecording spell with ingredients: {ingredients2}")
        spell_result2 = record_spell("Storm Call", ingredients2)
        print("Spell Result:", spell_result2)
    except AttributeError as e:
        print(f"AttributeError: {e}")

    print("\nTesting spell recording with validation:")
    try:
        spell_name = "Healing Rain"
        ingredients = "water,earth,air"
        print(f"Recording spell: {spell_name} with ingredients: {ingredients}")
        spell_result = record_spell(spell_name, ingredients)
        print("Spell Result:", spell_result)
    except AttributeError as e:
        print(f"AttributeError: {e}")

    print("\nTesting late import technique:")
    try:
        from alchemy.grimoire.spellbook import record_spell

        spell_name = "Mystic Breeze"
        ingredients = "air,fire"
        print(f"Recording spell: {spell_name} with ingredients: {ingredients}")
        spell_result = record_spell(spell_name, ingredients)
        print("Spell Result:", spell_result)
    except AttributeError as e:
        print(f"AttributeError: {e}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    circular_curse_breaking()
