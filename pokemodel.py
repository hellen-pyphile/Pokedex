import json
import requests
import os
from pokecontroller import add_pokemon
from pokecontroller import clean_screen

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
    new = {
        "id" = data['id'],
        "name" = data['name'], 
        "level" = level, 
        "types" = [t['type']['name'] for t in data['types']]
    }
    
    pokedex.append(new_pokemon)
    save_pokedex(pokedex)
    print(f"\nSucesso!\n\n{data['name'].capitalize()} foi adicionado à POKEDEX.")
    
def update_pokemon():
    clean_screen()
    pokedex = load_pokedex
    
    if not pokedex:
        print("Sua POKEDEX esta vazia.")
        
        busca = input("Digite o POKEMON ou seu ID: ").strip().lower()
        
        if not busca:
            print("\n\nPor favor, preencha o campo requisitado.")
            return
            
        for p in pokedex:
        #busca o Pokémon no seu arquivo JSON
        if str(p['id']) == busca or p['name'].lower() == busca:
            encontrado = True
            print(f"\nModificando: {p['name'].capitalize()} (Nível atual: {p['level']})")

            while True:
                new_name = input("Novo Pokémon (Nome/ID) (Enter para manter o atual): ").strip().lower()

                if not new_name:
                    break # se apertou Enter, sai do loop e mantém o atual

                url = f"https://pokeapi.co/api/v2/pokemon/{new_name}"
                try:
                    print("Consultando a PokeAPI...")
                    response = requests.get(url)
                    response.raise_for_status()
                    data = response.json()

                    new_id = data['id']

                    # verifica se o novo Pokémon já existe na Pokédex (ignorando o que esta editando)
                    if new_id != p['id'] and any(poke['id'] == new_id for poke in pokedex):
                        print(f"Erro: O Pokémon {data['name'].capitalize()} já existe em outro slot da sua Pokédex!")
                        continue # pede o nome novamente

                    p['id'] = new_id
                    p['nome'] = data['name']
                    p['tipos'] = [t['type']['name'] for t in data['types']]
                    print(f"Sucesso! Identidade atualizada para {p['nome'].capitalize()} via API.")
                    break 

                except requests.exceptions.HTTPError:
                    print("Erro: Pokémon não encontrado na PokeAPI. Tente novamente.")
                except requests.exceptions.ConnectionError:
                    print("Erro de conexão com a API. Verifique a internet.")
                    break #sai do loop em caso de erro de rede

            new_level_str = input(f"Novo nível para {p['nome'].capitalize()} (Enter para manter): ").strip()
            if new_level_str:
                try:
                    p['nivel'] = int(new_level_str)
                except ValueError:
                    print("Nível inválido. Mantendo o original.")

            save_pokedex(pokedex)
            print(f"\nOperação concluída e salva com sucesso!")
            break