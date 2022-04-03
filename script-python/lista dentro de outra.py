temp = list()
defi = list()
c = mai = men = 0
while True:
    temp.append(str(input('Nome: '))) # alocação 0
    temp.append(float(input('Peso: '))) #alocação 1
    if len(temp) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    defi.append(temp[:])
    temp.clear()
    e = str(input('Deseja continuar? [S/N]: '))
    if e in 'Nn':
        break
print('-' * 60)
print(f'Pessoas cadastradas: {len(defi)}.')
print(f'O maior peso foi de {mai}Kg. Pesos de: ', end='')
for p in defi:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {men}Kg. Peso de: ', end='')
for p in defi:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
print()        
    
