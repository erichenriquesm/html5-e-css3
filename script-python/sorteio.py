n1 = input('PRIMEIRO NOME:')
n2 = input('SEGUNDO NOME:')
n3 = input('TERCEIRO NOME:')
n4 = input('QUARTO NOME:')
lista = [n1 , n2 , n3 , n4]
from random import choice
escolhido = choice(lista)
print(f'O escolhido foi {escolhido})')
