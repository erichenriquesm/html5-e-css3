from datetime import date
ano = int(input('DIGITE O ANO DE NASCIMENTO: '))
atual = date.today().year
idade = atual - ano
print(f'QUEM NASCEU EM {ano} TEM {idade} ANOS EM {atual}')
if atual - ano == 18:
    print('\033[1;32mVOCÊ TEM QUE SE ALISTAR IMEDIATAMENTE!')
elif atual - ano < 18:
    saldo = 18 - idade
    print(f'\033[1;32mVOCÊ TEM {idade} ANOS AINDA FALTAM {saldo} ANOS PARA O ALISTAMENTO!')
    saldo = atual + saldo
    print(f'SEU ALISTAMENTO SERÁ EM {saldo}')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'\033[1;31mVOCÊ JÁ DEVRIA TER SE ALISTADO HÁ {saldo} ANOS!')
    print(f'SEU ALISTAMENTO FOI NO ANO {ano}')