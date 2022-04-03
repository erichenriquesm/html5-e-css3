sexo = str(input('Por favor, digite seu sexo: [M/F] ')).strip().upper()[0]
if sexo == 'M':
    s = 'Masculino'
else:
    s = 'Femenino'
while sexo not in 'MF':
    sexo = str(input('Sexo inválido, por favor tente novamente: [M/N] ')).strip().upper()[0]
    if sexo == 'M':
        s = 'Masculino'
    else:
        s = 'Femenino'
print(f'Sexo {s} defenido com sucesso!')    
