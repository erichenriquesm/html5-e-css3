'x² = a   b = x c = numero'
from math import sqrt
while True:
    a = int(input('Valor de x²: '))
    b = int(input('Valor de x: '))
    c = int(input('Valor de c: '))
    delta = b ** 2 + -4 * a * c
    xmais = (-1 * b + sqrt(delta)) / 2 * a
    xmenos = (-1 * b - sqrt(delta)) / 2 * a
    print(f'O delta é de {delta}. O x1 é igual a {xmais:.2f}. E o x2 é igual a {xmenos:.2f}')
    print('-' * 30)
    e = str(input('Deseja repetir? [S/N]: ')).strip().upper()[0]
    if e != 'S':
        break
print('Programa Finalizado! :)')
