print('-=-' *20)
print('JOGO DE ADIVINHA, TENTE VENCER O PROGRAMA!')
print('-=-' *20)
from time import sleep
from random import randint
computador = randint(0,5)
jogador = input('TENTE ADIVINHAR:')
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS, VOCÊ ADIVINHOU!')
else:
    print('QUE PENA! VOCÊ ERROU.')
print(f'EU PENSEI NO NÚMERO {computador}')
