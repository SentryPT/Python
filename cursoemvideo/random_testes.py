n1 = input('Digite um numero por favor: ')
n2 = input('Digite novamente um numero por favor: ')
s = float (n1) + float (n2)
#indicar o tipo que se quer definir, antes da variavel e a variavel fica ()
print (f'A soma entre {n1} e {n2} é igual a: {s}')
print (n1.isalnum)

# usamos as {} para selecionar uma variavel. apos isso fazemos .format para as chamar por ordem
# f é mais simples para chamar a variavel.



horapt = int (input('Indique a hora em Portugal: '))
horaes = int (horapt) + 1
print (type(horapt))
print('A hora em Espanha é: ' , horaes)



x= 'mariana'
print (type (x))

n = (int(input('Indique um número:')))
print(f'O número indicado é: {n} O antecessor é {n-1} e o sucessor é {n+1}')


n = (int(input('Indique um número: ')))
print(f'A raiz quadrada do número é: {n**(1/2)}')
print(f'O dobro do número é: {n*2}')
print(f'O triplo do número é: {n*3}')

print('Este programa irá converter um valor em metros e converter em cm e mm')
m = float(input('Insira o valor em metros: '))
print(f'O Valor em metros é: {m}, em cm é: {m * 100} e em mm é: {m * 1000}')

n = int(input('Insira um número para mostrar a sua tabuada:'))
print(f'1 x {n} é = a {n * 1}')
print(f'2 x {n} é = a {n * 2}')
print(f'3 x {n} é = a {n * 3}')
print(f'4 x {n} é = a {n * 4}')
print(f'5 x {n} é = a {n * 5}')
print(f'6 x {n} é = a {n * 6}')
print(f'7 x {n} é = a {n * 7}')
print(f'8 x {n} é = a {n * 8}')
print(f'9 x {n} é = a {n * 9}')
print(f'10 x {n} é = a {n * 10}')


print('- Cálculo de area de parede para pintura -')
alt = float(input('Indique a altura da parede: '))
larg = float( input('Indique a largura da parede:'))
area= larg*alt
print(f' Para pintar a seguinte área {area} m2, são necessários {area/2} l de tinta ')


