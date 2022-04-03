somaidade = 0 #a soma de todas as idades
mediaidade = 0# é a somaidade / por 4
maioridadehomem = 0
nomevelho = ' '
totmulher20 = 0
for p in range(1, 5):
    print('-=' * 14)
    print(f'{p}° pessoa')
    n = str(input('Nome da pessoa: '))
    i = int(input('Idade da pessoa: '))
    s = str(input('Sexo da pessoa [M/F]: ')).strip()
    somaidade += i
    if p == 1 and s in 'Mm': #O "IN 'Mn' SIGNIFICA" significa que tanto o m maiúsculo quanto o minúsculo serve
        maioridadehomem = i
        nomevelho = n
    if s in 'Mm'and i > maioridadehomem:
        maioridadehomem = i
        nomevelho = n
    if s in 'Ff' and i < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho.title()}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
