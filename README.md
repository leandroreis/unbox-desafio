# Desafio UNBOX

Este projeto contém o resultado do desafio para concorrer a vaga de desenvolvedor Python na UNBOX CULTURE.

## Instalação

Para rodar o projeto é necessário ter o Docker instalado: https://www.docker.com/products/docker-desktop

Execute utilizando Docker compose:
```sh
docker-compose up
```

## API

Uma vez que a aplicação esteja rodando, os seguintes endpoints estarão disponíveis:

- http://127.0.0.1:5000/partidas/timeout - Exibe quantas partidas terminam por time out (1000 rodadas);
- http://127.0.0.1:5000/partidas/media-turnos - Exibe quantos turnos em média demora uma partida;
- http://127.0.0.1:5000/jogadores/porcentagens - Exibe qual a porcentagem de vitórias por comportamento dos jogadores;
- http://127.0.0.1:5000/jogadores/vencedor - Exibe qual o comportamento que mais vence.


### Swagger
Para acessar a documentação da API acesse: http://127.0.0.1:5001


## Resultado

**Quantas partidas terminam por time out (1000 rodadas)?**  
Resposta: 45

**Quantos turnos em média demora uma partida?**  
Resposta: 453 

**Qual a porcentagem de vitórias por comportamento dos jogadores?**  
Resposta:
- Jogador aleatorio: 1.33%
- Jogador cauteloso: 71.33%
- Jogador exigente: 12.33%
- Jogador impulsivo: 15.00%

**Qual o comportamento que mais vence?**  
Resposta: Jogador cauteloso