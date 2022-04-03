'''p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
for c in range(p, d + r, r):   
    print(c , end=' → ')
print('Acabou')
'''


'''p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
while cont <= 10:
    print(f'{termo}', end=' → ')
    termo += r
    cont += 1
print('FIM')'''

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total +
    mais  
    while cont <= total:      
            print(f'{termo}', end=' → ')
            termo += r
            cont += 1
            print('PAUSA')
            mais = int(input('Quantos termos você quer mostrar a mais?'))
print(f'A progressão foi finalizada com {total} termos mostrados')

