import json

DATASET = "pokedex.json"

def load_pokedex():
    if os.path.exists(DATASET):
        with open(DATASET, "r", encoding='UTF-8') as f:
            try:    
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_pokedex():
    with open(DATASET, "w", encoding='UTF-8') as f:
        json.dump(pokedex, f, indent=4, ensure_ascii=False)
        