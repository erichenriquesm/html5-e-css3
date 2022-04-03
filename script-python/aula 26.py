f = str(input('DIGITE UMA FRASE:')).lower().strip()
print('A letra "a" aparece {} vezes.'.format(f.count('a')))
print('A primeira letra  "a" apareceu na posição {}'.format(f.find('a')+1))
print('A ultima aparição da letra "a" esta na posição {}'.format(f.rfind('a')+1))
