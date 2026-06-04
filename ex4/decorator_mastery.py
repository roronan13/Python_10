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

        print(f"Spell completed in {ending_time - starting_time:.3f} seconds.")

        return result

    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):

            given_power = args[-1]
            if given_power >= min_power:
                return func(*args, **kwargs)
            return ("Insufficient power for this spell.")

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_attempts:
                        print(f"Spell failed ({e}) , retrying ... (attempt {attempt}/{max_attempts}).")
                    else:
                        return (f"Spell casting failed ({e}) after {max_attempts} attempts.")

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 2 and name.replace(" ", "").isalpha():
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power.")


@spell_timer
def spell_throwing(spell: str) -> str:
    time.sleep(0.2)
    return (f"Spell {spell} has been thrown !")


if __name__ == "__main__":

    test_powers = [14, 20, 19, 25]
    spell_names = ['fireball', 'blizzard', 'freeze', 'shield']
    mage_names = ['Ash', 'Nova', 'Phoenix', 'Riley', 'Jordan', 'Sage']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("     Spell timer   \n")

    print(f"{spell_throwing(random.choice(spell_names))}")

    print("\n     Retrying spell   \n")

    
