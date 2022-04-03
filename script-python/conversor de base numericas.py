num = int(input('DIGITE UM NÚMERO INTEIRO: '))
print('''ESCOLHA A BASE PARA CONVERTER O NÚMERO:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opção = int(input('DIGITE SUA OPÇÃO: '))
if opção == 1:
    print(f'\033[1;35m{num} CONVERTIDO PARA BINÁRIO É IGUAL A {bin(num)[2:]}!')   #bin(x) para converter um número em binário, mais [2:] para pular as 2 primeiras casas desnecessárias.

elif opção == 2:
    print(f'\033[1;35m{num} CONVERTIDO EM OCTAL É IGUAL A {oct(num)[2:]}!')   # oct(x) para converter o número para octal mais, [2:] para pular as 2 primeiras casas desnecessárias.

elif opção == 3:
    print(f'\033[1;35m{num} CONVERTIDO EM HEXADECIMAL É IGUAL A {hex(num)[2:]}!')    # hex(x) para converter o número para hexadecimal mais, [2:] para pular as 2 primeiras casas desnecessárias.
else:
    print('\033[1;31mOPÇÃO INVÁLIDA TENTE NOVAMENTE!')

