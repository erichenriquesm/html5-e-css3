print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro  segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:     #para formar um triângulo a soma de qualquer segmento tem q ser menor q a soma das outras duas.
    print('Os segmentos acima PODEM formar um triângulo')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos NÃO PODEM formar um triângulo')


