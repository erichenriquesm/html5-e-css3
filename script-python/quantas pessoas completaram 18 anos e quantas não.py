from datetime import date
cont = 0
con = 0
for c in range(1, 8):
    nas = int(input(f'Em que ano a {c}° nasceu?: '))
    atual = date.today().year
    idade = atual - nas
    if idade >= 18:
        cont += 1
    else:
        con += 1
print(f'Ao todo tivemos {cont} pessoas maiores de idade!')
print(f'E {con} pessoas menores de idade!')
