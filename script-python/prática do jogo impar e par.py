from random import randint
v = 0
print('=-' * 30)
print('JOGO DO ÍMPAR E PAR')
print('=-' * 30)
while True:
    j = int(input('Digite um valor: '))
    com = randint(0, 10)
    t = j + com
    e = str(input('PAR OU ÍMPAR? [P/I]: ')).strip().upper()[0]
    print(f'VOCÊ ESCOLHEU {j} E O COMPUTADOR {com}! NO TOTAL DEU {t}')
    while e not in 'PI':
        e = str(input('PAR OU ÍMPAR? [P/I]: ')).strip().upper()[0]
    if e == 'P':
        if t % 2 == 0:
            print('VOCÊ VENCEU! PARABÉNS!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif e == 'I':
        if t % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar mais uma vez...')
print(f'GAME OVER! VOCÊ ACERTOU {v} VEZES')    
