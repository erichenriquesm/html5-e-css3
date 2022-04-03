lojas = [['Produtos'], ['Preço']]
while True:
    lojas[0].append(str(input('Digite o nome do produto: ')))
    lojas[1].append(float(input('Digite o preço: R$')))
    e = str(input('Quer continuar?[S/N]: '))
    if e in 'Nn':
        break
print(f'{lojas[0]:.<15}')
print(f'{lojas:>5.2f}')
