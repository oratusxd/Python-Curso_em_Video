'''
Exercício Python 33: Faça um programa que leia três números e
mostre qual é o maior e qual é o menor.
'''
n1 = int(input('Coloque o primeiro número: '))
n2 = int(input('Coloque o segundo número: '))
n3 = int(input('Coloque o terceiro número: '))
lista = [n1, n2 , n3]
print('O menor valor digitado foi',min(lista))
print('O maior valor digitado foi',max(lista))
# Você pode fazer com base nos if, menor e maior, mas né kkk