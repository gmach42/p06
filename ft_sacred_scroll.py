import alchemy


def test_sacred_scroll() -> None:
    """
    Demonstrate package exposure control via __init__.py in alchemy module.
    """

    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    try:
        print("alchemy.elements.create_fire(): ", end="")
        print(alchemy.elements.create_fire())
        print("alchemy.elements.create_water(): ", end="")
        print(alchemy.elements.create_water())
        print("alchemy.elements.create_earth(): ", end="")
        print(alchemy.elements.create_earth())
        print("alchemy.elements.create_air(): ", end="")
        print(alchemy.elements.create_air())
    except AttributeError:
        print("AttributeError: not exposed")

    print("\nTesting package-level access: (controlled by __init__.py):")
    try:
        print("alchemy.create_fire(): ", end="")
        print(alchemy.create_fire())
    except AttributeError:
        print("AttributeError: not exposed")
    try:
        print("alchemy.create_water(): ", end="")
        print(alchemy.create_water())
    except AttributeError:
        print("AttributeError: not exposed")
    try:
        print("alchemy.create_earth(): ", end="")
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError: not exposed")
    try:
        print("alchemy.create_air(): ", end="")
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError: not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    test_sacred_scroll()
