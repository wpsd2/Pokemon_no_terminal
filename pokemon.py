import random

class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10


    def __str__(self):
        return (f"{self.nome} lv{self.level}!")


    def atacar(self, pokemon):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))
        pokemon.vida = pokemon.vida - ataque_efetivo
        print(f"{pokemon} perdeu {ataque_efetivo} de vida  ")

        if pokemon.vida <= 0:
            print(f"{pokemon} foi derrotado :( ")
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = "Eletrico"
    def atacar(self, pokemon):
        print(f"{self} Atacou com choque do trovão {pokemon} ")
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = "Fogo"
    def atacar(self, pokemon):
        print(f"{self} Lancou uma bola de fogo em {pokemon}")
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = "Água"
    def atacar(self, pokemon):
        print(f"{self} Lancou um jato de d'água em {pokemon}")
        return super().atacar(pokemon)


