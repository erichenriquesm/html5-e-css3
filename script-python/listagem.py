listagem = ('lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 6,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
             'Caneta', 3,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for posição in range(0, len(listagem)):
    if posição % 2 == 0:
        print(f'{listagem[posição]:.<30}', end='')
    else:
        print(f'R${listagem[posição]:>7.2f}')
print('-' *40)
