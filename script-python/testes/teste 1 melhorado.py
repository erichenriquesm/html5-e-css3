p = 0
while True:
    print('-' * 40)
    p += 1
    n = str(input(f'Digite o nome da {p}° pessoa: ')).strip().title()
    i = int(input('Idade: '))
    p = float(input('Peso da pessoa: Kg'))
    print(f'{n}\n{i} anos\n{p}Kg')
    print('-' * 40)
    e = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if e != 'S':
        break
