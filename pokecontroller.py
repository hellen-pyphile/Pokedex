#pokecontroller.py
import os
import requests

import pokemodel
from pokemodel import load_pokedex, save_pokedex, new_pokemon

from IPython.display import clear_output

api_url = "https://pokeapi.co/api/v2/pokemon/"
timeout = 10

def clean_screen():
    if clear_output is not None:
        try:
            clear_output(wait=True)
        except ImportError:
            pass
    os.system('cls' if os.name == 'nt' else 'clear')

#exceptions for requests in error cases
def fetch_pokemon(query):
    response = requests.get(f"{api_url}{query}", timeout=timeout)
    return response.json()

#input level verification
def read_level(prompt):
    level_str = input(prompt).strip()
    if not level_str:
        return None
    level = int(level_str)
    if level < 1:
        raise ValueError
    return level
     
def add_pokemon():
    clean_screen()
    add = input("Adicionar um novo POKEMON (nome ou ID): ").strip().lower()
    
    #empty input
    if not add:
        input("\nPokecampo não pode estar vazio! Preencha o campo.")
        return
    
    try:
        print("Buscando '{add}'...")
        data = fetch_pokemon(add)
        
        pokedex = load_pokedex()
        new_id = data['id']
        
        #prevents duplicates
        if any(p['id'] == new_id for p in pokedex):
            print("\n\tErro!!\n\nO POKEMON:")
            print(f"\n- {data['name'].capitalize()} (ID: {new_id} já está na sua POKEDEX!)")
            return
        
        level = read_level(f"Digite o nível do seu {data['name'].capitalize()}: ")
        if level is None:
            print("\n\tErro!")
            print("\nO POKELEVEL não pode estar vazio.")
            return
            
        #talvez de problema
        entry = new_pokemon(data, level)
        print(f"\nSucesso!\n\n{entry['name'].capitalize()} foi adicionado à POKEDEX.")
        
    except requests.exceptions.HTTPError:
        print("\n\tErro!\n\nPokémon não encontrado na PokeAPI.")
    except ValueError:
        print("\n\tErro!\n\nO nível deve ser um número inteiro válido.")
    except requests.exceptions.ConnectionError:
        print("\n\tErro!\n\nFalha de conexão. Verifique sua internet.")
    except requests.exceptions.Timeout:
            print("\n\tErro!\n\nA PokeAPI demorou demais para responder.")
    except requests.exceptions.RequestException:
        print("\n\tErro!\n\nFalha inesperada ao consultar a PokeAPI.")
        
        
#register pokemon
def reg_pokemon():
    clean_screen()
    pokedex = load_pokedex()
    
    if not pokedex:
        print("Sua pokedex está vazia.\nVá capturar novos POKEMONS!")
    else:
        print("\t[MINHA POKEDEX]")
        
        #talvez de erro
        for p in sorted(pokedex, key=lambda x: x['id']):
            types = ", ".join(p['types'])
            print(f"#{p['id']:03d} | {p['name'].capitalize():<12} | Nível: {p['level']:<3} | Tipos: {pokemodel.types}")
        print("-" * 55)
        
def update_pokemon():
    clean_screen()
    pokedex = load_pokedex()

    if not pokedex:
        print("Sua POKEDEX está vazia.")
        return

    search = input("Digite o POKEMON ou seu ID: ").strip().lower()
    if not search:
        print("\n\nPor favor, preencha o campo requisitado.")
        return

    for p in pokedex:
        if str(p["id"]) == search or p["name"].lower() == search:
            print(f"\nModificando: {p['name'].capitalize()} (Nível atual: {p['level']})")

            while True:
                new_name = input("Novo Pokémon (Nome/ID)\n(Enter para manter o atual): ").strip().lower()
                if not new_name:
                    break  #enter: mantém o atual

                try:
                    print("Consultando PokeAPI...")
                    data = fetch_pokemon(new_name)
                    new_id = data["id"]

                    # impede duplicata com outro slot (ignora o próprio)
                    if new_id != p["id"] and any(o["id"] == new_id for o in pokedex):
                        print(f"Erro!\n\n{data['name'].capitalize()} já existe em outro slot da sua Pokédex!")
                        continue

                    p["id"] = new_id
                    p["name"] = data["name"]
                    p["types"] = [t["type"]["name"] for t in data["types"]]
                    print(f"Sucesso!\n\nIdentidade atualizada para {p['name'].capitalize()}.")
                    break

                except requests.exceptions.HTTPError:
                    print("Erro!\n\nPokémon não encontrado na PokeAPI. Tente novamente.")
                except requests.exceptions.RequestException:
                    print("Erro de conexão com a API.\nVerifique a internet.")
                    break  # sai do loop em caso de erro de rede

            try:
                new_level = read_level(f"Novo nível para {p['name'].capitalize()} (Enter para manter): ")
                if new_level is not None:
                    p["level"] = new_level
            except ValueError:
                print("Nível inválido. Mantendo o original.")

            save_pokedex(pokedex)
            print("\nOperação concluída e salva com sucesso!")
            return

    print("POKEMON não encontrado na POKEDEX.")

def remove_pokemon():
    clean_screen()
    pokedex = load_pokedex()
    if not pokedex:
        print("Sua Pokédex está vazia.")
        return

    search = input("Digite o ID do Pokémon para remover: ").strip()
    if not search:
        print("\nErro!\n\nO ID não pode estar vazio!")
        return

    try:
        id_remove = int(search)
    except ValueError:
        print("\nErro!\n\nPor favor, digite um ID numérico válido.")
        return

    if any(p["id"] == id_remove for p in pokedex):
        save_pokedex([p for p in pokedex if p["id"] != id_remove])
        print(f"\nPokémon com ID {id_remove} foi deletado da Pokédex.")
    else:
        print(f"\nID {id_remove} não consta na sua Pokédex.")
