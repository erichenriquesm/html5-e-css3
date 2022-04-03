gastotot = produtok = pmaisbarato = cont = 0
nomemaisbarato = ''
while True:
    n = str(input('Nome do Produto: ')).strip().title()
    p = float(input('Preço: R$'))
    cont += 1
    gastotot += p
    if p > 1000:
        produtok += 1
    elif cont == 1:
        pmaisbarato = p
        nomemaisbarato = n
    else:
        if p < pmaisbarato:
            pmaisbarato = p
            nomemaisbarato = n
    e = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if e == 'N':
        break
print(f'O total da compra deu R${gastotot}')    
print(f'Temos {produtok} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemaisbarato} custando R${pmaisbarato}')
