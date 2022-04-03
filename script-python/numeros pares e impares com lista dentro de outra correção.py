num = [[], []]
v = 0
for c in range(1, 8):
    v = int(input(f'{c}o. Valor: '))
    if v % 2 == 0:
        num[0].append(v)
    else:
        num[1].append(v)
num[0].sort()
num[1].sort()
print('-' * 60)
print(f'Os números pares são: {num[0]}')
print(f'Os números ímpares são: {num[1]}')
