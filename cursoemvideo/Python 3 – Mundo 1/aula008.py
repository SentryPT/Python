#Informação que vamos recolher durante a aula 08

# o comando import vai selecionar tudo da lib. se fizermos from lib import só se escolhe um elemento

import math
num = int(input('Digite um número'))
raiz = math.sqrt(num)
print(f'A raiz de um {num} é: {math.ceil(raiz)} ') 
#podemos adicionar dentro da {} a função para neste caso indicar que queremos arredondar para cima


#vamos importar a lib random e vamos mostrar um numero real aleatório entre 0 e 1
import random
num = random.random()
print(num)

import emoji
print (emoji.emojize('Sei que o bro Alex fica louco com a :banana: do Ben e só quer ir para a :bed: dele'))

