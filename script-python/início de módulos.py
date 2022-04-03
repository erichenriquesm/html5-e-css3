print('Calcular hipotenusa')
from math import hypot
co = float(input('O comprimento do cateto oposto:'))
ca = float(input('O comprimento do cateto adjacente '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
