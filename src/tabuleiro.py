from src.propriedade import Propriedade


class Tabuleiro:

    def __init__(self, posicoes=20):
        self.__posicoes = posicoes
        self.__propriedades = [Propriedade(i) for i in range(posicoes)]

    def nova_posicao(self, posicao, valor_dado, callback_volta):
        resultado = posicao + valor_dado

        if resultado >= self.__posicoes:
            callback_volta()
            return resultado - self.__posicoes

        return resultado

    def propriedade(self, posicao):
        return self.__propriedades[posicao]
