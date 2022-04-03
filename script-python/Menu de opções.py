n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:  
    print('''
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
''')
    escolha = int(input('Escolha: '))
    if escolha == 1:
        print(n1 + n2)
    elif escolha == 2:
        print(n1 * n2)
    elif escolha == 3:
        if n1 > n2:
            print(n1)
        if n2 > n1:
            print(n2)
        if n1 == n2:
            print('Os dois são iguais')
    elif escolha == 4:
        while escolha != 5:
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
            print('''
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
            ''')
            escolha = int(input('Escolha: '))
            if escolha == 1:
                    print(n1 + n2)
            elif escolha == 2:
                    print(n1 * n2)
            elif escolha == 3:
                if n1 > n2:
                     print(n1)
                if n2 > n1:
                     print(n2)
                if n1 == n2:
                    print('Os dois são iguais')    
print('Fim do programa')        
   
    
