a = int(input('\033[1;31mDIGITE UM VALOR: '))
b = int(input('DIGITE UM VALOR: '))
c = int(input('DIGITE UM VALOR: '))
#verificar o valor menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'\033[1;35mO MENOR VALOR É {menor}')
#verifiar maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'\033[1;35mO MAIOR VALOR É {maior}')
