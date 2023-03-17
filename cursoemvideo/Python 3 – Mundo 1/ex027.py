#programa que lê o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str (input('Indique o seu nome completo: ')).strip()
n = nome.split()
print(f"O seu primeiro nome é: { n [0] } e o seu apelido é {n [-1]}") 
#o [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim por diante