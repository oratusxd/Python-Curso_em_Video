import math
'''
Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do 
cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.


catetoO = float(input('Coloque a medida do cateto oposto: '))
catetoA = float(input('Coloque a medida do cateto adjacente: '))
hip = ((catetoO**2) + (catetoA**2))**(1/2)
print(f'A hipotenusa vai medir hip:.2f')'''
#Resolução importando o math
catetoO = float(input('Coloque a medida do cateto oposto: '))
catetoA = float(input('Coloque a medida do cateto adjacente: '))
hip = math.hypot(catetoO,catetoA)
print(f'A hipotenusa vai medir {hip:.2f}')
