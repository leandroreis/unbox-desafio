from random import shuffle

from src.jogador import *


class Jogadores:

    def __init__(self):
        self.__jogadores = [
            Impulsivo(),
            Exigente(),
            Cauteloso(),
            Aleatorio(),
        ]

    def sorteia(self):
        shuffle(self.__jogadores)

    def restantes(self):
        return [jogador for jogador in self.__jogadores if jogador.continua()]

    def vencedor(self, desempate=False):
        if len(self.restantes()) == 1:
            return self.restantes()[0]

        if desempate:
            return max(self.restantes(), key=lambda j: j.saldo())
