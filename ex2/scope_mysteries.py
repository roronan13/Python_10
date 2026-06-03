from collections.abc import Callable


def mage_counter() -> Callable:
    i: int = 0

    def counter() -> int:
        nonlocal i
        i += 1
        return i

    return counter


def spell_accumulator(initial_power: int) -> Callable:

    def accumulator()
        
    return a


# def enchantment_factory(enchantment_type: str) -> Callable:


# def memory_vault() -> dict[str, Callable]:


if __name__ == "__main__":

    print("     Mage counter   ")

    counter_a: Callable = mage_counter()
    counter_b: Callable = mage_counter()

    print(f"counter_a : {counter_a()}")
    print(f"counter_a : {counter_a()}")
    print(f"counter_b : {counter_b()}")
    print(f"counter_a : {counter_a()}")
    print(f"counter_b : {counter_b()}")

