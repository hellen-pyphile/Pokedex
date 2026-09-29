#pokemondel.py
import json
import requests
import os
import pokecontroller 

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

pokedex = load_pokedex()

def save_pokedex():
    with open(DATASET, "w", encoding='UTF-8') as f:
        json.dump(pokedex, f, indent=4, ensure_ascii=False)
        
        
def new_pokemon():
    new : {
        "id"  data['id'],
        "name" = data['name'], 
        "level" = level, 
        "types" = [t['type']['name'] for t in data['types']]
        }
    
    pokedex.append(new_pokemon)
    save_pokedex(pokedex)
    print(f"\nSucesso!\n\n{data['name'].capitalize()} foi adicionado à POKEDEX.")
    
            
def remove_pokemon():
    pokecontroller.clean_screen()
    pokedex = load_pokedex()
    if not pokedex:
        print("Sua Pokédex está vazia.")
        return

    busca = input("Digite o ID do Pokémon para remover: ").strip()

    #entrada vazia
    if not busca:
        print("\nErro!\n\n O ID não pode estar vazio!")
        return

    try:
        id_remove = int(busca)

        # Verifica se o ID realmente existe antes de recriar a lista
        if any(p['id'] == id_remove for p in pokedex):
            # Cria uma nova lista excluindo o Pokémon escolhido
            nova_pokedex = [p for p in pokedex if p['id'] != id_remove]
            save_pokedex(nova_pokedex)
            print(f"\nPokémon com ID {id_remove} foi deletado da Pokédex.")
        else:
            print(f"\nID {id_remove} não consta na sua Pokédex.")

    except ValueError:
        print("\nErro: Por favor, digite um ID numérico válido.")