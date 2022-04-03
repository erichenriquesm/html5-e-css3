altura = float(input('SUA ALTURA: '))
peso = float(input('DIGITE SEU PESO: KG'))
imc = peso / (altura * altura)
if imc <= 18.5:
    print('\033[1;31mVOCÊ ESTA ABAIXO DO PESO! SEU IMC É DE {:.1f}'.format(imc))
elif imc <= 25:
    print('\033[1;32mVOCÊ ESTÁ NO PESO IDEAL! SEU IMC É DE {:.1f}'.format(imc))
elif imc <= 30:
    print('\033[1;33mVOCÊ ESTÁ SOBRE PESO! SEU IMC É DE {:.1f}'.format(imc))
elif imc <= 40:
    print('\033[1;31mVOCÊ ESTÁ COM OBESIDADE! SEU IMC É DE {:.1f}'.format(imc))
else:
    print('\033[1;31mVOCÊ ESTÁ COM OBESIDADE MÓRBIDA! SEU IMC É DE {:.1f}'.format(imc))
