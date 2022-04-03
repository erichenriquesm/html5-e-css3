lista = ('Rafael', 'Roberto', 'Victor')
for c in range(1, 99999999):
    nome = str(input('Nome: ')).title()
    if nome == lista:
        print('É um nome bem comum')
    else:
        print('Belo nome')
