#Crie um program que leia um número real qualquer pelo teclado e mostre a sua porção inteira
#Ex: digite um número: 6.127            O número 6.127 tem a parte inteira 6

import math
num = float(input('Digite um número: '))
num_int = math.floor(num)
print (f'O número {num} tem a parte inteira {num_int}')