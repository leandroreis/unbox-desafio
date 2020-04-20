class Jogador:

    def __init__(self):
        self.__tipo = self.__class__.__name__
        self.__posicao = -1
        self.__saldo = 300
        self.__propriedades = []

    def tipo(self):
        return self.__tipo

    def get_posicao(self):
        return self.__posicao

    def set_posicao(self, posicao):
        self.__posicao = posicao

    def debita(self, valor):
        self.__saldo -= valor

    def credita(self, valor):
        self.__saldo += valor

    def saldo(self):
        return self.__saldo

    def add_propriedade(self, propriedade):
        self.__propriedades.append(propriedade)

    def rem_propriedade(self, propriedade):
        self.__propriedades.remove(propriedade)

    def compra(self, propriedade):
        self.debita(propriedade.valor_venda())
        self.add_propriedade(propriedade)
        propriedade.set_proprietario(self)

    def aluga(self, propriedade):
        self.debita(propriedade.valor_aluguel())
        propriedade.get_proprietario().credita(propriedade.valor_aluguel())

    def completa_volta(self):
        self.credita(100)

    def continua(self):
        return self.__saldo >= 0

    def deixa_partida(self):
        for propriedade in self.__propriedades:
            propriedade.set_proprietario(None)
        self.__propriedades = []
