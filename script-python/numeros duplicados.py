lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print(f'Valor já registrado! Não irei pôr novamente')
    e = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if e == 'N':
        break
lista.sort()    
print(f'Você digitou os valores: {lista}')      
