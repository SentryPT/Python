# Comentários e anotações referente à aula 10

tempo = int (input('Quantos anos tem o seu carro?'))
if tempo <= 3:
    print('O seu carro é novo!')
else:
    print(' O seu carro é velho...')
    
    
nome = str (input('Qual é o seu nome? '))
if nome == 'Luis':
    print('Mas que belo nome pá! ')
else:
    print(f'És tão básico {nome}. ')
print(f'Tem um bom dia {nome}, pá! ')

n1 = float (input('Qual a sua primeira nota? '))
n2 = float (input('Qual a sua segunda nota?'))
m = (n1 + n2) / 2
if m >9.5:
    print(f'Felizmente a nota de {m :.3} deu para ter positiva')
else:
    print(f'Infelizmente com a nota de {m :.3} és um burro do crl')