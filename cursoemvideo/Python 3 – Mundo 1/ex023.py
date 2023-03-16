#Separando dígitos de um número
num = int(input('Indique um número: '))
u = num // 1 % 10 #divide por 1 e tira o resto da divisão por 10
d = num // 10 % 10 #divide por 10 e tira o resto da divisão por 10
c = num // 100 % 10 #divide por 100 e tira o resto da divisão por 10
m = num // 1000 % 10 #divide por 1000 e tira o resto da divisão por 10
print(f'Analisando o seguinte número: {num}')
print(f'Unidades: {u}') 
print(f'Dezenas: {d}') 
print(f'Centenas: {c}') 
print(f'Milhares: {m}') 