from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Create the Philosopher's Stone using lead and a healing potion."""
    lead_to_gold_result = lead_to_gold()
    healing_potion_result = healing_potion()
    return (
        f"Philosopher's stone created using {lead_to_gold_result} "
        f"and {healing_potion_result}"
    )


def elixir_of_life() -> str:
    """Brew the Elixir of Life for eternal youth."""
    return "Elixir of life: eternal youth achieved!"
