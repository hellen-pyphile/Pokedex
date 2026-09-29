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
def fectch_pokemon(query):
    response = requests.get(f"{api_url}{query}", timeout=timeout)
    return response.json

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
        data = fectch_pokemon()
        
        pokedex = load_pokedex()
        new_id = data['id']
        
        #prevents duplicates
        if any(p['id'] == new_id for p in pokedex):
            print("\n\tErro!!\n\nO POKEMON:")
            print(f"\n- {data['name'].capitalize()} (ID: {new_id} já está na sua POKEDEX!)")
            return
        
        level = read_level(f"Digite o nivel do seu {data['name'].capitalize()}: ")
        if level is None:
            print("\n\tErro!")
            print("\nO POKELEVEL não pode estar vazio.")
            return
            
        #talvez de problema
        entry = new_pokemon(data, level)
        print(f"\nSucess0!\n\n{entry['name'].capitalize} foi adicionado à POKEDEX.")
        
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
        
        for p in sorted(pokedex, key=lambda x: x['id']):
            types = ", ".join(p['tipos'])
            print(f"#{p['id']:03d} | {p['nome'].capitalize():<12} | Nível: {p['nivel']:<3} | Tipos: {pokemodel.types}")
        print("\t" * 55)
        
        