n = 0
cont = 0
ntot = n
maior = 0
menor = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        cont += 1
        ntot += n          
print(f'Foram digitados {cont} números e a soma dos mesmsos é igual a {ntot} ')

