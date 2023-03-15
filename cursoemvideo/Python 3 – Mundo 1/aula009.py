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

#Para substituir, é o seguinte: 
frase = 'Grande pitao pa. É uma linguagem incrível'
frase.replace('pitao' , 'c++')