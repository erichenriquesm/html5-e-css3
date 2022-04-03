palavras = ('arvore', 'rio', 'peixe', 'areia')
for p in palavras:
    print(f'\nNa palavra {p.upper()} tem as vogais ', end='')
    for l in p:
        if l in 'aeiou':
            print(l, end=' ')
