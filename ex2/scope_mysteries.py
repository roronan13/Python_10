from collections.abc import Callable
import random


def mage_counter() -> Callable:
    i: int = 0

    def counter() -> int:
        nonlocal i
        i += 1
        return i

    return counter


def spell_accumulator(initial_power: int) -> Callable:

    def accumulator(amount_to_add: int) -> int:
        nonlocal initial_power
        initial_power += amount_to_add
        return initial_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchantment(item_name: str) -> str:
        return (f"{enchantment_type} {item_name}")

    return enchantment


def memory_vault() -> dict[str, Callable]:
    stored_values: dict = {}

    def store(key: str, value) -> None:
        stored_values[key] = value

    def recall(key: str) -> str:
        if key in stored_values:
            return (f"{stored_values[key]}")
        else:
            return ("Memory not found.")

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":

    initial_powers = [59, 63, 23]
    power_additions = [19, 9, 20, 6, 11]
    enchantment_types = ['Shocking', 'Flaming', 'Earthen']
    items_to_enchant = ['Sword', 'Ring', 'Staff', 'Wand']

    print("     Mage counter   ")

    counter_a: Callable = mage_counter()
    counter_b: Callable = mage_counter()

    print(f"counter_a : {counter_a()}")
    print(f"counter_a : {counter_a()}")
    print(f"counter_b : {counter_b()}")
    print(f"counter_a : {counter_a()}")
    print(f"counter_b : {counter_b()}")

    print("\n     Spell accumulator   ")

    accumulator: Callable = spell_accumulator(10)
    print(f"{accumulator(5)}")
    print(f"{accumulator(5)}")
    print(f"{accumulator(5)}")
    print(f"{accumulator(5)}")

    print("\n     Enchantment factory   ")

    enchantment: Callable = enchantment_factory(random.choice(enchantment_types))
    print(f"{enchantment(random.choice(items_to_enchant))}")
    enchantment: Callable = enchantment_factory(random.choice(enchantment_types))
    print(f"{enchantment(random.choice(items_to_enchant))}")
    enchantment: Callable = enchantment_factory(random.choice(enchantment_types))
    print(f"{enchantment(random.choice(items_to_enchant))}")
    enchantment: Callable = enchantment_factory(random.choice(enchantment_types))
    print(f"{enchantment(random.choice(items_to_enchant))}")
    enchantment: Callable = enchantment_factory(random.choice(enchantment_types))
    print(f"{enchantment(random.choice(items_to_enchant))}")

    print("\n     Memory vault     ")

    vault: dict[str, Callable] = memory_vault()

    print("Store 'best_number' = 13")
    vault['store']("best_number", 13)

    print("Recall 'best_number' : ", end="")
    print(f"{vault['recall']('best_number')}")
    print("Recall 'better_number' : ", end="")
    print(f"{vault['recall']('better_number')}")
