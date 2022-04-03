from random import randint
num = (randint(1,10), randint(1,10), randint(1,10),
       randint(1,10), randint(1,10))
print(f'Os números escolhidos foram {num}')
print(f'O maior número é {max(num)} e o menor é {min(num)}')
