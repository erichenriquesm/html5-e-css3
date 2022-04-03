import pygame
from random import randint
from time import sleep
pygame.init()
pygame.mixer.music.load('é madrugada e você está ouvindo lofi para dormir.mp3')
pygame.mixer.music.play()
pygame.event.wait()

print('\033[1;33m-=-\033[m' * 20)
print('                     \033[1;35mJOGO ENVOLVENTE\033[m')
print('\033[1;33m-=-\033[m' * 20)

print('ESCOLHA UM NÚMERO DE 1 A 5')
for c in range(0, 1000):
    tentativa = int(input('TENTE ADIVINHAR O VALOR ESCOLHIDO: '))
    computador = randint(1,5)
    print('ESCOLHENDO...')
    sleep(2)
    if tentativa == computador:
        print(f'VOCÊ ACERTOU! O NÚMERO ESCOLHIDO FOI {computador}')
    else:
        print(f'QUE PENA, VOCÊ ERROU, O NÚMERO ESCOLHIDO FOI {computador}')
print('FIM')    


