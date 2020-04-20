from random import randrange

from src.jogador import Jogador


class Aleatorio(Jogador):

    def compra(self, propriedade):
        if randrange(1) % 2:
            super().compra(propriedade)
