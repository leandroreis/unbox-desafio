from src.jogador import Jogador


class Exigente(Jogador):

    def compra(self, propriedade):
        if propriedade.valor_aluguel() > 50:
            super().compra(propriedade)
