resposta = 'S'
soma =  cont = media = maior = menor = 0
while resposta in 'Ss':
    n = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media =  soma / n
print('Foram postos {} valores e a média foi de {:.2f}'.format(cont, media))                        
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
