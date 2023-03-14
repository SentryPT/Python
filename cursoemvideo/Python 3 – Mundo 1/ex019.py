#exercicio de Sorteando um item de uma lista! 
import random
alunos = ['André' , 'Mara' , 'Luis' , 'Josué']
print(random.choice(alunos))


#Faz uma lista de ordenação de apresentação:
import random
n1 = str(input('Indique um aluno: '))
n2 = str(input('Indique o segundo aluno: '))
n3 = str(input('Indique o terceiro aluno: '))
n4 = str(input('Indique o quarto aluno: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem é a seguinte: ')
print(lista)
