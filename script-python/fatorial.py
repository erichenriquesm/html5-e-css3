while True:
    fator = int(input('Fator de: '))
    r = 1
    for f in range(1, fator + 1):
        r *= f
    print(f'{fator}! = {r}')
    e = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if e != 'S':
        break
print('Programa finalizado.')    
