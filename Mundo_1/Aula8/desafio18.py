import math
'''
Exercício Python 18: Faça um programa que leia um ângulo 
qualquer e mostre na tela o valor do seno, cosseno e tangente 
desse ângulo.
'''
angulo = int(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O seno de {angulo} é : {seno:.2f}')
print(f'O cosseno de {angulo} é: {cosseno:.2f}')
print(f'O cosseno de {angulo} é: {tangente:.2f}')
