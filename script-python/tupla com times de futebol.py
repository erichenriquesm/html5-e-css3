time = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Bragantino', 'Fortaleza',
        'Corinthians', 'Internacional', 'Fluminence', 'Cuiabá', 'Athletico-PR',
        'América-MG', 'São Paulo', 'Atlético-GO', 'Ceará-SC', 'Santos',
        'Bahia', 'Sport Recife', 'Juventude', 'Grêmio', 'Chapecoense')
print(f'Lista de times do brasileirão: {time}')
print('-' * 30)
print(f'Os 5 primeiros colocados são: {time[:5]}')
print('-' * 30)
print(f'Os últimos 4 colocados são: {time[16:20]}')
print('-' * 30)
print(f'Times em ordem alfabética: {sorted(time)}')
print('-' * 30)
print(f'Chapecoense está na {time.index("Chapecoense")+ 1}° colocação')
