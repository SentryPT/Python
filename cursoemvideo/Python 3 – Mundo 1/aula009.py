#Informação que vamos recolher durante a aula 09

#Slicing Text
#Relativamente ao range, o último valor não entra na contagem
frase = 'Grande pitao pa. É uma linguagem incrível'
frase[9:15]
#Resultado será: tao pa

#Neste caso, irá mostrar do 9 ao 21, dois a dois. Os restantes vão sendo ignorados
frase = 'Grande pitao pa. É uma linguagem incrível'
frase [9:21:2]

#Aqui, irá mostrar a frase a partir do 5º até ao fim. Se fosse :5 mostraria até ao 5º elemento
frase = 'Grande pitao pa. É uma linguagem incrível'
frase [5:]

#Análise de strings. Lenght da frase
frase = 'Grande pitao pa. É uma linguagem incrível'
len(frase)

#Análise. Faz a contagem de O de 0 até 13
frase = 'Grande pitao pa. É uma linguagem incrível'
frase.count('o' , 0, 13)

#Análise: Indica em que posição foi encontrada a string indicada.
frase = 'Grande pitao pa. É uma linguagem incrível'
frase.find('de')

#Análise: Se dentro da frase, existe ou não a palavra pesquisada
frase = 'Grande pitao pa. É uma linguagem incrível'
'pitao' in frase

#.lower ou upper, coloca em minúsculas ou maiúsculas
#.capitalize vai colocar todas as iniciais em maiúsculas
#.title vê quantas palavras tem e após cada espaço, coloca a inicial em maiúscula

#.strip vai remover todos os espaços inúteis no início e no fim
# se colocarmos   .rstrip    vai remover os espaços à direita
# Se fosse o lstrip é o da esquerda
frase = '       Grande pitao pa. É uma linguagem incrível          '
frase.rstrip()

#na divisão de strings é o seguinte: 
    #.split() vai criar uma divisão em cada espaço das strings.
    
    

#ex22
nome = str (input('Indique o seu nome completo: ')).strip()
print('Analisando o seu nome....')
print(f'o seu nome em maiusculas é: {nome.upper()}'  )
print(f'O seu nome em minúsculas é: {nome.lower()}' )
print(f"O seu nome tem ao todo {len(nome)-nome.count(' ')} letras")  



#ex25
nome = str(input('Indique o seu nome completo: ')).strip()
print(f"O seu nome tem Silva? {('silva' in nome.lower())}")

#ex26 - fazemos o upper, para por todas as palavras em caps e faz a conta
frase = str(input('Escreva uma frase à sua escolha: ')).strip().upper()
print(f"A letra A surge {frase.count('A')} vezes ")
print(f"A letra A surge na {frase.find('A') + 1}ª posição ")
print(f" A letra A surge em último na posição {frase.rfind('A')}") #aqui vai procurar a partir do lado direito, posição final
print(frase)


#ex 27
n = str(input('Indique o seu nome completo: ')).strip()
nome = n.split() # vai dividir o nome inteiro em partes
print(nome)
print(f' O seu primeiro nome é {nome[0]} e o seu apelido é {nome [-1]}')
