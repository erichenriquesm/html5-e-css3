print('{:=^40}'.format('LOJA DO ERIC :)'))
p = float(input('PREÇO DAS COMPRAS R$'))
print('''FORMAS DE PAGAMENTO.
[1] À VISTA/CHEQUE                  
[2]À VISTA NO CARTÃO                      
[3]2X NO CARTÃO                       
[4]3X OU MAIS NO CARTÃO''')      #10% DE DESCONTO,  5% DE DESCONTO , PREÇO NORMAL , + 20%.
opção = int(input('QUAL SUA OPÇÃO DE PAGAMENTO? '))
if opção == 1:
    saldo = p - (p * 10 / 100)
    print(f'\033[1;35mÀ VISTA COM O DESCONTO DE 10%, A COMPRA SAI POR {saldo}!')
elif opção == 2:
    saldo = p - (p * 5 / 100)
    print(f'\033[1;35mÀ VISTA NO CARTÃO COM O DESCONTO DE 5%, A COMPRA SAI POR R${saldo} ')
elif opção == 3:
    duas = p / 2
    print(f'\033[1;35mVALOR DA COMPRA: 2X DE R${duas}')
elif opção == 4:
    saldo = p + (p * 20 / 100)
    parcelas = int(input('QUANTAS PARCELAS? '))
    total = saldo / parcelas

    print(f'EM {parcelas} PARCELAS  NO CARTÃO, A COMPRA SAIRÁ POR {total}! ')


