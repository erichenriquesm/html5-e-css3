from random import randint
v = 0
print('=-' * 16)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 16)
while True:
    jogada = int(input('Digite um valor: '))
    com = randint(0, 10)
    t = jogada + com
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {jogada} e o computador {com}. Total de {t}')    
    if escolha == 'P':
        if t % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif escolha == 'I':
        if t % 2 == 1:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Gamer Over! Você venceu {v} vezes')    

        
