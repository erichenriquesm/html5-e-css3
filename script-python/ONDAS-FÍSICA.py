from math import sqrt
print('-' *40)
print('''[1]CALCULADOR DE PERÍODO
[2]CALCULADOR DE FREQUÊNCIA
[3]CALCULADOR DE COMPRIMENTO DA ONDA
[4]CALCULADOR DE COMPRIMENTO MHZ COM VELOCIDADE DA LUZ 3.10^8
[5]RAZÃO ENTRE DUAS VELOCIDADES
[6]DENSIDADE LINEAR
OBS: A VÍRGULA NÃO FUNCIONA NO PROGRAMA, USE UM PONTO PARA UM VALOR QUEBRADO.
EXEMPLO: 2,6 = 2.6''')
print('-' *40)
while True:
    e = int(input('Digite uma opção: '))
    while e > 6:
         e = int(input('Digite uma opção válida: '))
    print('-' *40)    
    if e == 1:
        f = float(input('Digite a frequência: '))
        p = 1 / f
        print(f'{p:.2f}s')
        print('-' *40)
        
    if e == 2:
        p = float(input('Digite o período: s'))
        f = 1 / p
        print(f'{f:.2f}Hz')
        print('-' *40)
    
    if e == 3:
        v = float(input('Digite a velocidade de propagação: [M/S] '))
        f = float(input('Digiti a frequência: Hz '))
        c = v / f
        print(f'{c:.2f}m')
        print('-' *40)
        
    if e == 4:
        f = float(input('Digite a frequência: MHz '))
        lam = (3 / f) * 100
        print(f'{lam:.0f}m ou {lam}m')
        print('-' *40)
        
        
    if e == 5:
        v1 = float(input('Primeira velocidade: '))
        v2 = float(input('Segunda velocidade: '))
        r = v1 / v2
        print(f'A razão entre {v1}m e {v2}m é de {r}m')
        print('-' *40)
        
    if e == 6:
        d = float(input('Digite a densidade linear sem a exponenciação: '))
        n = float(input('Digite a força: N '))
        r = (n / d) * 100
        raiz = sqrt(r)
        print(f'A velocidade de propagação é de {raiz}m/s')
        print('-' *40)

