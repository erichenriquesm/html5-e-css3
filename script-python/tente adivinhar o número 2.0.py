from random import randint
print('----- Olá, sou seu dispositivo! Tente acertar o número de 0 a 10! -----')
c = randint(0, 10)
tentativas = 0
acertou = False
while not acertou:
    j = int(input('Digite um número: '))
    c = randint(0, 10)
    if j == c:
        acertou = True
    else:
        if j > c:
            print('Ponha menos ae...')
        else:
            print('Ponha mais ai...')
    tentativas += 1     
print(f'Até você acertar foram {tentativas} tentativas!')

    
        
