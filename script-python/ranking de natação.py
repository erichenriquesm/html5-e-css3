from datetime import date
while True:
    ano = int(input('DIGITE O ANO DE NASCIMENTO: '))
    atual = date.today().year
    idade = atual - ano
    if idade <= 9:
        print(f'O ATLETA TEM {idade} ANOS.\nCLASSIFICAÇÃO: \033[1;34mMIRIM!')
    elif  idade <= 14:
        print(f'O ATLETA TEM {idade} ANOS.\nCLASSIFICAÇÃO: \033[1;33mINFANTIL!')
    elif idade <= 19:
        print(f'O ATLETA TEM {idade} ANOS.\nCLASSIFICAÇÃO: \033[1;36mJUNIOR!')
    elif idade <= 25:
        print(f'O ATLETA TEM {idade} ANOS.\nCLASSIFICAÇÃO: \033[1;32mSÊNIOR!')
    else:
        print(f'O ATLETA TEM {idade} ANOS.\nCLASSIFICAÇÃO: \033[1;35mMASTER!')

    e = str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()[0]
    if e != 'S':
        break
print('PROGRAMA FINALIZADO!')
