#exercicio de cálculo quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60€ por dia e 0,15€ por Km rodado
print('Vamos calcular a quantidade de km percorridos e os dias que foi alugado')
km = float(input('Quantos km percorreu com a viatura? '))
dias = int(input('Quantos dias teve o carro alugado? '))
preco_dias = dias * 60
preco_km = km * 0.15
preco = preco_dias + preco_km
print(f'Quando for entregar a viatura, terá que efetuar o pagamento de {preco} €')