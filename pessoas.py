import random

from pokemon import *


NOMES = ["João", "José", "Pedro", "Maria", "Mathes", "Matias", "Morais", "Mauro", "Marcio", "Beto", "Breno", "Brenda"]
POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Charmilion"),
    PokemonFogo("Charizard"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Wartotle"),
]

class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        self.pokemons = pokemons

        self.dinheiro = dinheiro


    def __str__(self):
        return self.nome


    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}!".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print(f"{index} - {pokemon}")
        else:
            print("{} não tem pokemons". format(self))


    def escolher_pokemon(self):

        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f"{self} escolheu {pokemon_escolhido}!")
            return pokemon_escolhido
        else:
            print("Esse player não tem Pokemons.")


    def mostrar_dinheiro(self):
        print(f"Você tem ${self.dinheiro}!")


    def ganhar_dinheiro(self, quantidade):
        self.dinheiro = self.dinheiro + quantidade
        print(f"Você ganhou {quantidade}!")
        self.mostrar_dinheiro()


    def batalhar(self, pessoa):
        print(f"{self} Iniciou uma batalha com {pessoa}!")
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f"{self} Ganhou a batalha!")
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print(f"{pessoa} Ganhou a batalha!")
                    break
        else:
            print("Falha inesperada:(")

class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} Capturou {}".format(self, pokemon))


    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha seu Pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print(f"{pokemon_escolhido} Eu escolho você!!!")
                    return pokemon_escolhido
                except:
                    print("Escolha invalida")
        else:
            print("Você não tem Pokemons.")


    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print(f"Um {pokemon} selvagem apareceu!")

            escolha = input(f"Deseja tentar capturar {pokemon}? (s/n): ")
            if escolha == 's':
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print(f"O {pokemon} escapou.")
            else:
                print(f"...")
        else:
            print("Nenhum Pokemon selvagem foi encontrado :(")

class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))
            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)

