# programa que lê o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str (input('Indique o seu nome completo: ')).strip()
print("O seu nome tem Silva?")
print(f"{('Silva' in nome.lower())}")