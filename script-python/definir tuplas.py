tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o ultimo  número: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apreceu na {tupla.index(3)+1}° posição')
else:
    print(' Onúmero 3 não foi digitado')
    
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
