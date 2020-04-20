from src.jogador import Jogador


class Cauteloso(Jogador):

    def compra(self, propriedade):
        if self.saldo() - propriedade.valor_venda() >= 80:
            super().compra(propriedade)