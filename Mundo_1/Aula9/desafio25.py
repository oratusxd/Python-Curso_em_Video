'''
Exercício Python 25: Crie um programa que leia o nome de uma 
pessoa e diga se ela tem “SILVA” no nome.
'''
nome = input('Qual é o seu nome completo? ').strip()
nome_min = nome.lower()
print('O seu nome tem Silva? ', 'silva' in nome_min)