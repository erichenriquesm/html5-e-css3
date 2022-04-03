an = float(input('DIGITE UM ÂNGULO:'))
from math import radians, sin, cos, tan
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print('o ângulo de {}º tem o SENO de {:.2f}'.format(an , seno )) 
print('COSSENO de {:.2f}'.format(cosseno))
print('TANGENTE de {:.2f}'.format(tangente))
