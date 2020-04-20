from random import randrange

from src.contador import Contador


class Partida:

    def __init__(self, tabuleiro, jogadores, rodadas_max=1000):
        self.tabuleiro = tabuleiro
        self.jogadores = jogadores
        self.rodadas = 0
        self.rodadas_max = rodadas_max
        self.vencedor = None

    @staticmethod
    def lanca_dado():
        return randrange(1, 6)

    def rodada(self):
        for jogador in self.jogadores.restantes():
            posicao_atual = jogador.get_posicao()
            dado = self.lanca_dado()
            posicao = self.tabuleiro.nova_posicao(posicao_atual, dado, jogador.completa_volta)
            jogador.set_posicao(posicao)

            propriedade = self.tabuleiro.propriedade(posicao)
            if not propriedade.get_proprietario():
                jogador.compra(propriedade)
            else:
                jogador.aluga(propriedade)

            if not jogador.continua():
                jogador.deixa_partida()

            Contador.turno()

    def valendo(self):
        self.rodadas += 1
        self.vencedor = self.jogadores.vencedor()
        return self.rodadas <= self.rodadas_max and not self.vencedor

    def comecar(self):
        while self.valendo():
            self.rodada()

        if not self.vencedor:
            self.vencedor = self.jogadores.vencedor(desempate=True)
            Contador.timeout()

        Contador.partida()
        Contador.vitoria(self.vencedor.tipo())
