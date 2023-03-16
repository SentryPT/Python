#Separando dígitos de um número
num = int(input('Indique um número: '))
n = str(num)
print(f'Analisando o seguinte número: {num}')
print(f'Unidades: {n[3]}') #digito 3 é a unidade
print(f'Dezenas: {n[2]}') # digito 2 é a dezena
print(f'Centenas: {n[1]}') # digito 1 é a centena
print(f'Milhares: {n[0]}') #digito 0 é o milhar