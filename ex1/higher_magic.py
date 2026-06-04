from collections.abc import Callable
import random


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner_function(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combiner_function


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier_function(target: str, power: int) -> str:
        print(f"\nOriginal power was {power}.")
        return (base_spell(target, power * multiplier))

    return amplifier_function


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_function(target: str, power: int) -> str:
        if condition(target, power):
            print(f"\nPower is {power}.")
            return (spell(target, power))
        else:
            print(f"\nPower is {power}.")
            return ("Spell fizzled.")

    return conditional_function


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_function(target: str, power: int) -> list[str]:
        print(f"\nSpells are {spells}.")
        actions_list: list[str] = []
        for spell in spells:
            actions_list.append(spell(target, power))

        return actions_list

    return sequence_function


if __name__ == "__main__":

    val = [21, 8, 7]
    targ = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    def heal(target: str, power: int) -> str:
        return (f"Heal restores {target} for {power} HP.")

    def attack(target: str, power: int) -> str:
        return (f"Attack removes {power} HP to {target}.")

    def explore(target: str, power: int) -> str:
        return (f"Explore gives +{power} vision to {target}.")

    def condition_function(target: str, power: int) -> bool:
        if power >= 20:
            return True
        return False

    combiner_function: Callable = spell_combiner(heal, attack)
    print(f"{combiner_function(random.choice(targ), random.choice(val))}")

    amplifier_function: Callable = power_amplifier(explore, 4)
    print(f"{amplifier_function(random.choice(targ), random.choice(val))}")

    conditional_function: Callable = conditional_caster(condition_function,
                                                        attack)
    print(f"{conditional_function(random.choice(targ), random.choice(val))}")

    sequence_function: Callable = spell_sequence([heal, attack, explore])
    print(f"{sequence_function(random.choice(targ), random.choice(val))}")
