n = int(input('Informe um número:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'ANALISANDO O NÚMERO {n}')
print('Unidade: {} \nDezena: {} \nCentena {} \nMilhar: {}'.format(u, d, c, m))
