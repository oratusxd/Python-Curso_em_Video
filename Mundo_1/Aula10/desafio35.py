'''
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'''
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
a = float(input('Coloque a primeira reta do triângulo: '))
b = float(input ('Coloque a segunda reta do triângulo: '))
c = float(input('Coloque a terceira reta do triângulo: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo') 
    