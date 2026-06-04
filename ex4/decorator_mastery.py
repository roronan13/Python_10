from functools import wraps
from collections.abc import Callable
import time
import random


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__} ...")

        starting_time = time.time()
        result = func(*args, **kwargs)
        ending_time = time.time()

        print(f"Spell completed in {round(ending_time - starting_time, 3)} seconds.")

        return result 

    return wrapper



# def power_validator(min_power: int) -> Callable:


# def retry_spell(max_attempts: int) -> Callable:


# class MageGuild:
#     @staticmethod
#     def validate_mage_name(name: str) -> bool:


    # def cast_spell(self, spell_name: str, power: int) -> str:


@spell_timer
def spell_throwing(spell: str) -> str:
    time.sleep(0.1)
    return (f"Spell {spell} has been thrown !")


if __name__ == "__main__":

    test_powers = [14, 20, 19, 25]
    spell_names = ['fireball', 'blizzard', 'freeze', 'shield']
    mage_names = ['Ash', 'Nova', 'Phoenix', 'Riley', 'Jordan', 'Sage']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("     Spell timer   \n")

    print(f"{spell_throwing(random.choice(spell_names))}")
