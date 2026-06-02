def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts: list[dict] = []

    sorted_artifacts = sorted(artifacts, key=lambda arti: arti["power"],
                              reverse=True)

    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages: list[dict] = []

    filtered_mages = list(filter(lambda mage: mage["power"] >= min_power,
                                 mages))

    return filtered_mages


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spells: list[str] = []

    transformed_spells = list(map(lambda spell: (f"* {spell} *"), spells))

    return transformed_spells


def mage_stats(mages: list[dict]) -> dict:
    stats: dict = {'max_power': int, 'min_power': int, 'avg_power': float}

    max_power: int = max(mages, key=lambda mage: mage["power"])["power"]
    min_power: int = min(mages, key=lambda mage: mage["power"])["power"]
    average_power: float = round((sum(mage["power"] for mage in mages)) /
                                 len(mages), 2)

    stats = {'max_power': max_power, 'min_power': min_power,
             'avg_power': average_power}

    return stats


if __name__ == "__main__":

    artifacts = [{'name': 'Ice Wand', 'power': 86, 'type': 'relic'},
                 {'name': 'Crystal Orb', 'power': 101, 'type': 'relic'},
                 {'name': 'Light Prism', 'power': 62, 'type': 'weapon'},
                 {'name': 'Ice Wand', 'power': 118, 'type': 'relic'}]
    mages = [{'name': 'Kai', 'power': 50, 'element': 'wind'},
             {'name': 'Riley', 'power': 59, 'element': 'earth'},
             {'name': 'Casey', 'power': 91, 'element': 'ice'},
             {'name': 'Morgan', 'power': 100, 'element': 'wind'},
             {'name': 'Zara', 'power': 59, 'element': 'shadow'}]
    spells = ['meteor', 'fireball', 'earthquake', 'tsunami']

    print("   artifact_sorter : \n")
    print(f"{artifacts}")
    print(f"{artifact_sorter(artifacts)}")

    print("\n   power_filter : \n")
    print(f"{mages}")
    print(f"{power_filter(mages, 60)}")

    print("\n   spell_transformer : \n")
    print(f"{spells}")
    print(f"{spell_transformer(spells)}")

    print("\n   mage_stats : \n")
    print(f"{mages}")
    print(f"{mage_stats(mages)}")
