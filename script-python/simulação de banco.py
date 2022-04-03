print('=' * 30)
print('SIMULAÇÃO DE BANCO')
print('=' * 30)
valor = int(input('Que valor você quer sacar?: R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50: # se cedula de 50 não der cedula recebe 20
            ced = 20
        elif ced == 20:# se cedula de 20 não der cedula recebe 10
            ced = 10
        elif ced == 10:# se cedula de 10 não der cedula recebe 1
            ced = 1
        totced = 0 # cada vez que mudar a cedula o total precisa voltar a zero para contar as cedulas individualmente
        if total == 0:
            break
