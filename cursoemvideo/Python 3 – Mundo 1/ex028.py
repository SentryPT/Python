#ex29. Das adivinhas
from random import randint
pc = randint (0 , 5)
jogador = int (input ('Indique um numero à sua escolha:'))
if jogador == pc:
    print(f'Acertou. Indicou {jogador} e o pc {pc} também! Ganhou um prémio')
else:
    print('Já foste! Falhaste.')