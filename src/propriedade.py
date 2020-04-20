from random import randrange


class Propriedade:

    def __init__(self, posicao):
        self.__posicao = posicao
        self.__valor_venda = randrange(70, 90)
        self.__valor_aluguel = randrange(40, 60)
        self.__proprietario = None

    def posicao(self):
        return self.__posicao

    def valor_venda(self):
        return self.__valor_venda

    def valor_aluguel(self):
        return self.__valor_aluguel

    def set_proprietario(self, proprietario):
        self.__proprietario = proprietario

    def get_proprietario(self):
        return self.__proprietario
