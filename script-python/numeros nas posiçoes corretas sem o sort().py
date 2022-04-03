lista = list()
for c in range(0, 5):
    n = int(input(f'Digite o {c}° valor: '))
    if c == 0 or n > list[-1]:
        lista.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adiconado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores em ordem são: {lista}')
