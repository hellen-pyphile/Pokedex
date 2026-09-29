#pokeview.py
import pokecontroller

def menu():
    while True:
        pokecontroller.clean_screen()
        print("\t POKÉDEX\n")
        print("[1] - Adicionar Pokémon (API)")
        print("[2] - Listar Meus Pokémon")
        print("[3] - Atualizar Dados")
        print("[4] - Remover Pokémon")
        print("[0] - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == '1':
            pokecontroller.add_pokemon()
        elif opcao == '2':
            pokecontroller.reg_pokemon()
        elif opcao == '3':
            pokecontroller.update_pokemon()
        elif opcao == '4':
            pokecontroller.remove_pokemon()
        elif opcao == '0':
            print("Desligando a Pokédex... Até logo!")
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")

#initializes application
if __name__ == "__main__":
    menu()