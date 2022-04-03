'''for c in range(1, 10):
    print(f'{c}° Pessoa')
    p = str(input('Nome: '))
    i = int(input('Idade: '))
    g = str(input('Gênero: [M/F]'))'''
ex = 1
cont = 0
cont18 = 0
contmenor = 0
maioridade = 0
nomevelho = ''
while ex != 0:
    cont += 1
    print(f'{cont}° pessoa')
    p = str(input('Nome: ')).strip().title()
    i = int(input('Idade: '))
    if i >= 18:
        cont18 += 1
        maioridade = i
        nomevelho = p
    elif i > maioridade:
            maioridade = i
            nomevelho = p
    else:
        contmenor += 1
    while i >= 112:
        i = int(input('Para de mentir sua idade e coloca essa porra direito: '))
        if i >= 18:
            cont18 += 1
            maioridade = i
            nomevelho = p
        elif i > maioridade:
            maioridade = 1
            nomevelho = p
        elif i <= 17:
            contmenor += 1        
    g = str(input('Gênero: [M/F]: ')).strip().upper()[0]
    while g not in 'MF':
        g = str(input('Gênero errado, tente novamente: [M/F]')).strip().upper()[0]    
    ex = int(input('Se deseja parar a execução do programa digite 0 se não qualquer outro número: '))
print(f'Foram registradas {cont} pessoas! {cont18} são de maior e {contmenor} são de menor!')
print(f'A pessoa mais velha se chama {nomevelho} e tem {maioridade} anos!')
