import json
from pokecontroller import add_pokemon

DATASET = "pokedex.json"

url = f"https://pokeapi.co/api/v2/pokemon/{add}"

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
        
        
def new_pokemon():
    new = {
        "id" = data['id'],
        "name" = data['name'], 
        "level" = level, 
        "types" = [t['type']['name'] for t in data['types']]
    }
    
    pokedex.append(new_pokemon)
    salve_pokedex(pokedex)