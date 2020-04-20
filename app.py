from flask import Flask
from flask_cors import CORS

from src.simulador import Simulador

app = Flask(__name__)
CORS(app)

Simulador.executa()


@app.route('/partidas/timeout')
def partidas_timeout():
    return {
        'data': Simulador.timeouts()
    }


@app.route('/partidas/media-turnos')
def partidas_media_turnos():
    return {
        'data': Simulador.media_turnos()
    }


@app.route('/jogadores/porcentagens')
def jogadores_porcentagens():
    return {
        'data': Simulador.porcentagens()
    }


@app.route('/jogadores/vencedor')
def jogadores_vencedor():
    return {
        'data': Simulador.vencedor()
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0')
