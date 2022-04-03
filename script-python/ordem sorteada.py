print('ORDEM ALEATÓRIA')
n1 = input('PRIMEIRO ALUNO PARA APRESENTAR:')
n2 = input('SEGUNDO ALUNO PARA APRESENTAR:')
n3 = input('TERCEIRO ALUNO PARA APRESENTAR:')
n4 = input('QUARTO ALUNO PARA APRESENTAR:')
lista = [n1 , n2 , n3 , n4]
from random import shuffle
shuffle(lista)
print('A ordem de sorteio é:')
print(lista)
       
