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
    

#ex 28
num = int (input('Escreva um número entre 0 e 5: '))
if num > 5:
    print(f'O valor que indicou, {num}, está errado. Tente novamente')
else:
    print(f'Acertou. {num} tinha sido o valor que eu tinha pensado.')
    
#ex28 resolução
from random import randint
pc = randint(0, 5) #cria num aleatorio
print('Irei pensar num valor')
jogador = int(input('O número que vou indicar é o seguinte: '))
if jogador == pc:
    print(f'Acertou no numero {pc}. Muitos parabéns!')
else:
    print(f'Já foste. Grande abraço')


#Ex29
vel = float (input('Indique a velocidade a que ia no carro:'))
if vel > 80:
    print(f'Foi apanhado a {vel}km/h. Foi multado por excesso de velocidade. ')
    multa = (vel - 80) * 7
    print(f' Terá de pagar uma multa no valor de {multa}€')
else:
    print(f'À velocidade a que vai, {vel}km/h, está dentro do limite legal.')
print('Conduza com segurança')

#Exercicio da taxa de alcool

print('-=-'*20)
print('Cálculo de taxa de alcool para saber se terá contra-ordenação')
print('-=-'*20)
tx_alcool = float ( input(' Indique a taxa de alcool no sangue: '))
if tx_alcool <= 0.49:
    print(f'Pois bem. Com uma taxa de {tx_alcool}, és um PedroGF45')
elif tx_alcool >= 0.5 and tx_alcool <= 0.79: 
    print(f'Pois é meu menino. Já levas de prémio entre 250€ a 1250€')
elif tx_alcool >= 0.8 and tx_alcool <= 1.2:
    print(f'A tua taxa de {tx_alcool}, é à Peneirol. Larga os 500€ até 2500€.')
elif tx_alcool >= 1.2:
    print(f'Oh maninho, com essa taxa de {tx_alcool}, já vais é de cana. Aquele abraço.')
print('Se conduzir, não beba')
print('-=-'*20)


altura = float (input('Indique a sua altura, em m:'))
peso = float (input('Indique o seu peso, em kg: '))
imc = peso / (altura * altura)
if imc <= 18.49:
    print(f'O seu imc de {imc :.2}, está no nivel de Magreza')
elif imc >= 18.5 and imc <= 24.9:
    print(f'O seu imc de {imc :.2}, está no nível de Normal')
elif imc >= 25 and imc <= 29.9:
    print(f'O seu imc de {imc :.2}, está no nível de Sobrepeso')
elif imc >= 30 and imc <= 34.9:
    print(f'O seu imc de {imc :.2}, está no nível de Obesidade Grau I')
elif imc >= 35 and imc <= 39.9:
    print(f'O seu imc de {imc :.2}, está no nível de Obesidade Grau II')
else:
    print(f'O seu imc de {imc :.2}, está no nível de Obesidade Grau III')

print('Promova um hábito de vida saudável, ingira acima de 2l de água por dia e realize atividade física diariamente. Por si, pela sua saúde.')


#ex30
num = int (input('Digite um número para saber se é par ou impar:'))
if num % 2 == 0:
    print(f'O {num} é um número par')
else:
    print(f'O {num} é um número impar.')