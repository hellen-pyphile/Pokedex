#pokemondel.py
import json
import os

DATASET = "pokedex.json"

#reads .json pokedex
def load_pokedex():
    if os.path.exists(DATASET):
        with open(DATASET, "r", encoding='UTF-8') as f:
            try:    
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

#saves pokedex list on .json
def save_pokedex(pokedex):
    with open(DATASET, "w", encoding='UTF-8') as f:
        json.dump(pokedex, f, indent=4, ensure_ascii=False)
        
        
def new_pokemon(data, level):
    pokedex = load_pokedex() #loads .json current version
    new = {
        "id" : data['id'],
        "name" : data['name'], 
        "level" : level, 
        "types" : [t['type']['name'] for t in data['types']]
        }
    
    pokedex.append(new_pokemon)
    save_pokedex(pokedex)
    return new