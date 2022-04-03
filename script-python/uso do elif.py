casa = float(input('O VALOR DA CASA: R$'))    #casa que vai ser comprada.
salário = float(input('SALÁRIO DO COMPRADOR: R$'))  #salário do comprador.
ano = int(input('QUANTIDADE DE ANOS PARA FINANCIAR: ')) #em quantos anos será pago.
prestação = casa / (ano * 12)
print('PARA PAGAR ESSA CASA DE R${} EM {} ANOS, A PRESTAÇÃO SERÁ DE R${:.2f} POR MÊS!'.format(casa , ano, prestação))
mínimo = salário * 30 / 100
if prestação <= mínimo:
    print('\033[1;32mVOCÊ PODERÁ FAZER ESSE FINANCIAMENTO!\033[m')
else:
    print('\033[1;31mVOCÊ NÃO PODERÁ FAZER ESSE FINANCIAMENTO!\033[m')

