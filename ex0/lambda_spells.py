def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts: list[dict] = []
    
    sorted_artifacts = sorted(artifacts, key=lambda arti: arti["power"], reverse=True)

    return sorted_artifacts

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages: list[dict]= []

    filtered_mages = filter(lambda mage: mage["power"] >= min_power, mages)

    return filtered_mages

def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spells: list[str] = []

    transformed_spells = map(lambda spell: (f"* {spell} *"), spells)

    return transformed_spells

def mage_stats(mages: list[dict]) -> list[dict]:
    