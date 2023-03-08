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


