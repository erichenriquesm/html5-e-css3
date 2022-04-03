ex = ''
while ex != 0:
    nota1 = float(input(' PRIMEIRA NOTA:'))
    nota2 = float(input(' SEGUNDA NOTA:'))
    media = (nota1 + nota2) / 2
    print('a média entre' , nota1 , 'e' , nota2 , f'é igual a {media}')
    ex = int(input('0 para sair ou qualquer número para continuar: '))
print('Programa finalizado')
