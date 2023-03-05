# Exercicio nº 3 do 2º capitulo do FreecodeCamp

hrs  = input('Insira as horas de trabalho: ')
rate  = input('Insira o valor que recebe por hor: ')
#tenho de colocar a variavel como int ou float, pq senao considera como string
pay = float (hrs) * float (rate)
print('Vai receber: ' , pay )