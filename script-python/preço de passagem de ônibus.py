km = float(input('DISTÂNCIA À SER CORRIDA EM KM/H:'))
print(f'VOCÊ ESTÁ PRESTES A COMEÇAR UMA VIAGEM DE {km}KM')
if km <= 200:
    v = km * 0.50
    print(f'O VALOR A SER PAGO SERÁ DE R${v}!')
else:
    v = km * 0.45
    print(f'O VALOR A SER PAGO É DE R${v}')
print('TENHA UMA BOA VIAGEM!')    

	
    
    
