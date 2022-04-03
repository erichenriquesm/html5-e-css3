print('\033[1;31mOlá, Seja Bem Vindo(a)\033[m')
s = float(input('\033[1;32mDIGITE SALÁRIO DO FUNCIONÁRIO R$'))
if s <= 1200:
    aumento = s + (s * 15/100)
    print(f'\033[1;33mO SALÁRIO DO FUNCIONÁRIO É DE R${s}, COM O AUMENTO ELE IRÁ RECEBER R${aumento}\033[m')
else:
    aumento = s + (s * 10 / 100)
    print(f'\033[1;35mO SALÁRIO DO FUNCIONÁRIO É DE R${s}, COM O AUMENTO ELE IRÁ RECEBER R${aumento}\033[m')



