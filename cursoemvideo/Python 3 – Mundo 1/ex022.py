#Ex

nome = str(input('Indique o seu nome completo: ')).strip()
print('Analisando os resultados: ')
print(f' O seu nome em maiúsculas é o seguinte: {nome.upper().strip()} ')
print(f' O seu nome em minúsculas é o seguinte: {nome.lower().strip()}')
print(f" O seu nome ao todo tem {len(nome) - nome.count(' ')} letras")
print(f" O seu primeiro nome tem {nome.find(' ')} letras")

separa = nome.split()
print(separa)
print(f' O seu primeiro nome é {separa[0]} e tem {len(separa)} letras')