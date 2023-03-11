#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa
import math
cat_a = float(input('Indique a medida do cateto adjacente: '))
cat_b = float(input('Indique a medida do cateto oposto: '))
print(f'O cateto adjacente é: {cat_a} e o cateto oposto: {cat_b}, logo a hipotenusa é: {(math.hypot(cat_a , cat_b)):.3f}')



#Calcular a hipotenusa sem a lib
cat_a = float(input('Qual a medida do cateto adjacente:'))
cat_b = float(input('Qual a medida do cateto oposto: '))
hipot = cat_a ** 2 + cat_b ** 2
print ( 'A hipotenusa do triângulo é:' )