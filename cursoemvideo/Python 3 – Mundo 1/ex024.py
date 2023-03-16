#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”
cid = str (input('Em que cidade é que nasceu?')).strip()
print(cid [:5] == 'Santo') #aqui vimos se até ao 5 caratér a palavra é igual a Santo