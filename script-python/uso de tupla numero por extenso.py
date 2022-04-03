cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    n = int(input('Digite um número de 0 a 20: '))
    while n < 0 or n > 20:
        n = int(input('Tente novamente. Digite  um número de 0 a 20: '))
    print(f'Você digitou o número {cont[n]}')    
    e = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if e == 'N':
        break
