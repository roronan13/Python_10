from collections.abc import Callable
from typing import Any
import random
from functools import reduce, partial, lru_cache
from operator import add, mul


class OperationError(Exception):
    def __init__(self, error_msg: str = "Unknown operation.") -> None:
        super().__init__(error_msg)


def base_enchantment(power: int, element: str, target: str) -> str:
    return (f"{power} of {element} is thrown at {target} !")


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation not in ['add', 'multiply', 'max', 'min']:
        raise OperationError(f"Unknown operation ({operation}).")

    if len(spells) == 0:
        return 0

    print(f"(Operation is {operation})")

    if operation == "add":
        return (reduce(add, spells))
    if operation == "multiply":
        return (reduce(mul, spells))
    if operation == "max":
        return (reduce(max, spells))
    else:
        return (reduce(min, spells))


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    ice = partial(base_enchantment, 50, "ice")
    fire = partial(base_enchantment, 50, "fire")
    mud = partial(base_enchantment, 50, "mud")

    return {
        "ice": ice,
        "fire": fire,
        "mud": mud
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return (memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1))


def spell_dispatcher() -> Callable[[Any], str]:
    


if __name__ == "__main__":

    spell_powers = [11, 30, 44, 39, 24, 13]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [17, 12, 17]

    print("     Spell reducer   \n")

    try:
        print(spell_reducer(spell_powers, random.choice(operations)))
    except OperationError as e:
        print(f"{e}")

    print("\n     Partial enchanter   \n")

    enchanter = partial_enchanter(base_enchantment)
    print(f"{enchanter['ice']('me')}")
    print(f"{enchanter['fire']('you')}")
    print(f"{enchanter['mud']('them')}")

    print("\n     Memoized fibonacci   \n")

    print(f"0 --> {memoized_fibonacci(0)}")
    print(f"1 --> {memoized_fibonacci(1)}")
    print(f"10 --> {memoized_fibonacci(10)}")
    print(f"15 --> {memoized_fibonacci(15)}")
    # print(memoized_fibonacci.cache_info())

    print("\n     Spell dispatcher   \n")

