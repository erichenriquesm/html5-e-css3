from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print('''SUAS OPÇÕES: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
computador = randint(0, 2)
jogada = int(input('QUAL É A SUA JOGADA? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogada]))
print('-=' * 11)
if computador == 0: # computador joga pedra
    if jogada == 0:
        print('EMPATE')
    elif jogada == 1:
        print('JOGADOR VENCE')
    elif jogada == 2:
        print('COMPUTADOR VENCE')
    else:
        print('OPÇÃO INVÁLIDA' )

elif computador == 1: # computador joga papel
    if jogada == 0:
        print('COMPUTADOR VENCE')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
        print('JOGADOR VENCE')
    else:
        print('OPÇÃO INVÁLIDA')

elif computador == 2: # computador joga tesoura
    if jogada == 0:
        print('JOGADOR VENCE')
    elif jogada == 1:
        print('COMPUTADOR VENCE')
    elif jogada == 2:
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA')
    
