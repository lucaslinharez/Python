"""
Como deixar o código mais limpo e fácil de ler

- Variaveis: Usar letras maiusculas para indicar que a variavel é constante
e não vai mudar ao longo do código. 

- Condições: muitas condições no mesmo if, prejudica a leitura e dificulta
o entendimento

- Blocos de código: muitos blocos causam complexidade na leitura, sempre tentar
facilitar a leitura.

"""

velocidade = 60
local_carro = 100


RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RANGE = 1 # distancia onde o radar pega, 1m antes e depois do 100

velocidade_passou = velocidade > RADAR_1
multa = local_carro >= (LOCAL_1 - RANGE) and local_carro <= (LOCAL_1 + RANGE) 

if velocidade_passou:
    print(f'Passou da velocidade: {RADAR_1}')

if multa and velocidade_passou:
    print('Carro multado | Radar 1') 


