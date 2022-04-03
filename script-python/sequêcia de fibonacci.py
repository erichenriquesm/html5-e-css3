print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
t = int(input('Digite quantos termos você deseja: '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}' , end='')
cont = 3     # o número 3 é explicado pq o primeiro e o segundo termo ja foram postos e irá começar do terceiro
while cont <= t:
    t3 = t1 + t2   
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
