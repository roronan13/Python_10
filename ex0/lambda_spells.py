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
