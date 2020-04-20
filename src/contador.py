class Contador:
    __partidas = 0
    __timeouts = 0
    __turnos = 0

    __vitorias = {
        'Aleatorio': 0,
        'Cauteloso': 0,
        'Exigente': 0,
        'Impulsivo': 0,
    }

    @staticmethod
    def partida():
        Contador.__partidas += 1

    @staticmethod
    def timeout():
        Contador.__timeouts += 1

    @staticmethod
    def turno():
        Contador.__turnos += 1

    @staticmethod
    def vitoria(tipo):
        Contador.__vitorias[tipo] += 1

    @staticmethod
    def partidas():
        return Contador.__partidas

    @staticmethod
    def timeouts():
        return Contador.__timeouts

    @staticmethod
    def turnos():
        return Contador.__turnos

    @staticmethod
    def vitorias():
        return Contador.__vitorias
