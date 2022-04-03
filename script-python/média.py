nota1 = float(input('DIGITE A PRIMEIRA NOTA: '))
nota2 = float(input('DIGITE A SEGUNDA NOTA: '))
média = (nota1 + nota2) /2
print(f'SUA MÉDIA FOI DE {média}')
if média < 5.0:
    print(f'\033[1;31m VOCÊ FOI REPRVADO, POIS SUA MÉDIA FOI ABAIXO DE 5.0!')
elif média >= 5 and média < 7:
    print('\033[1;31mVOCÊ FICOU DE RECUPERAÇÃO!')
else:
    print('\033[1;32mVOCÊ FOI APROVADO!')