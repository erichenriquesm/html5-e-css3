numeros = list()
for c in range(1, 8):
    numeros.append(int(input(f'{c}o. numero: ')))
numeros.sort()
print('-' * 60)
print('Os números pares foram:', end=' ')
for p in numeros:
    if p % 2 == 0:
        print(f'[{p}]', end=' ')
print()
print('Os numeros ímpares foram:', end=' ')
for p in numeros:
    if p % 2 == 1:
        print(f'[{p}]', end=' ')
print()        
        
