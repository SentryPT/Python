#ex 31 exercicio km
km = float (input ('Quantos km irá percorrer na viagem?'))
if km <= 200:
    valor = km * 0.05
    print(f'A distância percorrida de {km} km, tem um custo de {valor}€')
else:
    valor = km * 0.45
    print(f'A distância percorrida de {km} km, tem um custo de {valor}€')