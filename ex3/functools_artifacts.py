from collections.abc import Callable
from typing import Any
import random
from functools import reduce, partial
from operator import add, mul


class OperationError(Exception):
    def __init__(self, error_msg: str = "Unknown operation.") -> None:
        super().__init__(error_msg)


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
    

# def memoized_fibonacci(n: int) -> int:


# def spell_dispatcher() -> Callable[[Any], str]:



if __name__ == "__main__":

    spell_powers = [11, 30, 44, 39, 24, 13]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [17, 12, 17]

    print("     Spell reducer   \n")

    try:
        print(spell_reducer(spell_powers, random.choice(operations)))
    except OperationError as e:
        print(f"{e}")
