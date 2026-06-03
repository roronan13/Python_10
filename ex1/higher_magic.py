from collections.abc import Callable
import random


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner_function(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combiner_function


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier_function(target: str, power: int) -> str:
        print(f"Original power was {power}.")
        return (base_spell(target, power * multiplier))

    return amplifier_function


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_function(target: str, power: int) -> 

# def spell_sequence(spells: list[Callable]) -> Callable:


if __name__ == "__main__":

    test_values = [21, 8, 7]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    def heal(target: str, power: int) -> str:
        return (f"Heal restores {target} for {power} HP.")

    def attack(target: str, power: int) -> str:
        return (f"Attack removes {power} HP to {target}.")

    def explore(target: str, power: int) -> str:
        return (f"Explore gives +{power} vision to {target}.")

    combiner_function: Callable = spell_combiner(heal, attack)
    print(f"{combiner_function(random.choice(test_targets), random.choice(test_values))}")

    amplifier_function: Callable = power_amplifier(explore, 4)
    print(f"{amplifier_function(random.choice(test_targets), random.choice(test_values))}")
