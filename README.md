# 🔴 Pokédex CLI — Desafio 4 (Engenharia de Software)

Aplicação em linha de comando (CLI) desenvolvida em Python para gerenciar uma Pokédex local. O sistema realiza consultas à API pública [PokeAPI](https://pokeapi.co/) para validação e obtenção de dados oficiais dos Pokémons e mantém a persistência local em um arquivo `pokedex.json`.

---

## 📌 Visão Geral da Arquitetura

O projeto foi organizado seguindo o padrão de separação de responsabilidades (**MVC** simplificado), mantendo as regras de persistência desacopladas da interface de interação:

```
├── pokemodel.py        # Model: manipulação de dados, persistência e I/O com pokedex.json
├── pokecontroller.py   # Controller: lógica de validação, regras de negócio e integração com a PokeAPI
├── pokeview.py         # View: menu interativo e interface de entrada/saída no terminal
└── pokedex.json        # Arquivo de persistência local dos Pokémons cadastrados
```

### Papel de cada módulo:
- **`pokemodel.py` (Model):** Responsável exclusivo por carregar e persistir a lista de Pokémons no arquivo `pokedex.json`.
- **`pokecontroller.py` (Controller):** Faz a ponte entre a interface e o modelo. Valida entradas, consome a PokeAPI, garante IDs únicos e trata erros de rede.
- **`pokeview.py` (View):** Exibe as opções para o usuário via terminal e direciona as chamadas para o controlador.

---

## 📋 Estrutura dos Dados

Cada registro salvo no `pokedex.json` respeita o seguinte contrato de dados:

```json
{
  "id": 25,
  "nome": "pikachu",
  "tipos": ["electric"],
  "nivel": 15
}
```

---

## ⚙️ Funcionalidades

1. **Adicionar Pokémon:** Consulta o nome ou ID na PokeAPI, valida duplicatas de ID, solicita o nível e persiste no arquivo local.
2. **Listar Pokémons:** Apresenta todos os Pokémons cadastrados formatados em tabela, ordenados crescentemente pelo ID.
3. **Atualizar Pokémon:** Permite alterar o Pokémon cadastrado ou o seu nível atual mantendo a consistência dos dados.
4. **Remover Pokémon:** Exclui o registro correspondente ao ID informado.

---

## 🛡️ Regras de Negócio e Validações

- **ID Único:** Não é permitido adicionar um Pokémon cujo ID já esteja presente na Pokédex local.
- **Campos Obrigatórios:** Nomes e níveis vazios são rejeitados na entrada.
- **Tratamento de Exceções:** 
  - Tratamento para Pokémon inexistente na PokeAPI (`HTTPError`).
  - Tratamento para falhas de conexão de rede (`ConnectionError`).
  - Tratamento para entradas numéricas inválidas (`ValueError`).
  - Criação automática do `pokedex.json` caso o arquivo não exista ou esteja corrompido.

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior instalado.
- Biblioteca `requests`.

### Instalação das dependências

```bash
pip install requests
```

### Executando a aplicação

Inicie o sistema executando o ponto de entrada (`pokeview.py`):

```bash
python pokeview.py
```