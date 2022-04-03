c = c18 = chomem = cmulher = 0
print('REALIZAÇÃO DE CADASTRO')
while True:
    c += 1
    i = int(input(f'Idade da {c}° pessoa: '))
    if i >= 18:
        c18 += 1    
    s = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if s == 'M':
        chomem += 1
    if s == 'F':
        if i < 20:
            cmulher += 1        
    e = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if e != 'S':
        break
    print('-' * 30)
print(f'Há {c18} pessoas maiores de idade! {chomem} Homens foram cadastrados! {cmulher} mulheres têm menos de 20 anos!')        
print('Programa Finalizado! :)')        
