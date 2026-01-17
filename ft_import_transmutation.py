def import_transmutation_mastery():
    print("=== Import Transmutation Mastery ===\n")
    try:
        print("Method 1 - Full module import:")
        import alchemy.elements
        print("alchemy.elements.create_fire(): ", end="")
        print(alchemy.elements.create_fire())
    except AttributeError:
        print("AttributeError: not exposed")

    try:
        print("\nMethod 2 - Specific function import:")
        from alchemy.elements import create_water
        print("create_water(): ", end="")
        print(create_water())
    except AttributeError:
        print("AttributeError: not exposed")

    try:
        print("\nMethod 3 - Aliased import:")
        from alchemy.potions import healing_potion as heal
        print("heal(): ", end="")
        print(heal())
    except AttributeError:
        print("AttributeError: not exposed")

    try:
        print("\nMethod 4 - Multiple imports:")
        from alchemy.elements import create_earth, create_fire
        print("create_earth(): ", end="")
        print(create_earth())
        print("create_fire(): ", end="")
        print(create_fire())
        from alchemy.potions import strength_potion
        print("strength_potion(): ", end="")
        print(strength_potion())
    except AttributeError:
        print("AttributeError: not exposed")

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    import_transmutation_mastery()
