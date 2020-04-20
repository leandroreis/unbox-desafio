from src.contador import Contador
from src.jogadores import Jogadores
from src.partida import Partida
from src.tabuleiro import Tabuleiro


class Simulador:

    @staticmethod
    def executa(simulacoes=300):
        for simulacao in range(simulacoes):
            tabuleiro = Tabuleiro()

            jogadores = Jogadores()
            jogadores.sorteia()

            partida = Partida(tabuleiro=tabuleiro, jogadores=jogadores)
            partida.comecar()

        Simulador.console()

    @staticmethod
    def timeouts():
        return Contador.timeouts()

    @staticmethod
    def media_turnos():
        return Contador.turnos() // Contador.partidas()

    @staticmethod
    def porcentagens():
        resultado = dict()
        for tipo, vitorias in Contador.vitorias().items():
            resultado[tipo.lower()] = vitorias / Contador.partidas() * 100
        return resultado

    @staticmethod
    def vencedor():
        vitorias = Contador.vitorias()
        return max(vitorias, key=vitorias.get)

    @staticmethod
    def console():
        print('Quantas partidas terminam por time out (1000 rodadas)? R:', Simulador.timeouts())
        print('Quantos turnos em média demora uma partida? R:', Simulador.media_turnos())
        print('Qual a porcentagem de vitórias por comportamento dos jogadores? R:')
        for tipo, percentual in Simulador.porcentagens().items():
            print('- Jogador {0}: {1:.2f}%'.format(tipo, percentual))
        print('Qual o comportamento que mais vence? R:', Simulador.vencedor())
