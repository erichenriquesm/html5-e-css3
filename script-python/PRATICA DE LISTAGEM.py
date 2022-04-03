listagem = ('água', 2.75,
            'batata', 177,
            'carvão', 13)
print('-' * 40)
print(f'{"LISTAGEM DE COMPRAS":^40}')
print('-' * 40)
for p in range(0, len(listagem)):
    if p % 2 == 0:
        print(f'{listagem[p]:.<30}', end='')
    else:
        print(f'R${listagem[p]:>5.2f}')
print('-' * 40)
