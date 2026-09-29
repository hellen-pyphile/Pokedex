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

#errors exceptions for requests
def fectch_pokemon(query):
    response = requests.get(f"{api_url}{query}", timeout=timeout)
    return response.json


     
def add_pokemon():
    clean_screen()
    add = input("Adicionar um novo POKEMON (nome ou ID): ").strip().lower()
    
    #empty input
    if not add:
        input("\nPokecampo não pode estar vazio! Preencha o campo.")
        return
    
    url = f"https://pokeapi.co/api/v2/pokemon/{add}"
    
    try:
        print("Buscando '{add}'...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        pokedex = load_pokedex()
        new_id = data['id']
        
        #impede duplicatas
        if any(p['id'] == new_id for p in pokedex):
            print("\n\tErro!!\n\nO POKEMON:")
            print("\n- {data['name'].capitalize()} (ID: {new_id} já está na sua POKEDEX!)")
            return
        
        level_str = input(f"Digite o nivel do seu {data['name].capitalize()}: ").strip(): ")
        
        #empty level
        if not level_str:
            print("\n\tErro!")
            print("\nO POKELEVEL não pode estar vazio.")
            return
            
        level = int(level_str)
        
        pokemodel.new_pokemon()
        
    except requests.exceptions.HTTPError:
        print("\n\tErro!\n\nPokémon não encontrado na PokeAPI.")
    except ValueError:
        print("\n\tErro!\n\nO nível deve ser um número inteiro válido.")
    except requests.exceptions.ConnectionError:
        print("\n\tErro!\n\nFalha de conexão. Verifique sua internet.")
        
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
        
        