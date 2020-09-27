import pickle
# from pokemon import *
from pessoas import *


def escolher_pokemon_inicial(player):
    print("Escolha seu pokemon inicial! ")

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Escolha um dos três Pokemons iniciais: ")
    print("Aperte 1 para escolher o Pikachu")
    print("Aperte 2 para escolher o Charmander")
    print("Aperte 3 para escolher o Squirtle")

    while True:
        escolha = input("Escolha seu Pokemon: ").strip()

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Opção invalida!")


def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo Salvo com sucesso!")
    except Exception as error:
        print("Erro ao salvar o jogo")
        print(error)


def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Jogo carregado com sucesso")
            return player
    except Exception as error:
        print("Save não encontrado")
        print(error)


if __name__ == "__main__":
    print("Bem-Vindo ao Pokemon inicial")
    player = carregar_jogo()

    if not player:
        nome = input("Olá qual é seu nome? ")
        player = Player(nome)
        print("Olá essa é uma copia muito modesta dos jogos do pokemon, aonde não temos ainda um interface gráfica, apenas via terminal para relembrar")
        print(f"Seja bem vindo {player}")
        if player.pokemons:
            print("Esses são seus Pokemons!")
            player.mostrar_pokemons()
        else:
            print("Você não tem nenhum Pokemon, será preciso escolher um Pokemon: ")
            escolher_pokemon_inicial(player)
        print("Agora será preciso realizar uma batalha, para provar seu valor! ")
        Gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(Gary)
        salvar_jogo(player)

    while True:
        print("O que deseja fazer? ")
        print(" 1 Iniciar sua jornada Pokemon? ")
        print(" 2 Participar de uma batalha contra um adversário? ")
        print(" 3 Mostrar Pokeagenda ")
        print(" 0 Sair do jogo? ")
        escolha = input("Qual sua escolha? ").strip()
        if escolha == "0":
            print("Saindo do jogo...")
            break
        elif escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == "3":
            player.mostrar_pokemons()
        else:
            print("Escolha invalida")
