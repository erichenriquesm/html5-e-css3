print('Para parar a conta utilize o 0!)
pares = 0
v = int(input('Valor: '))
while v != 0:
    v = int(input('Valor: '))
    if v != 0:
        if v % 2 == 0:
            pares += 1
print(f'O sistema leu {pares} números pares!')        
