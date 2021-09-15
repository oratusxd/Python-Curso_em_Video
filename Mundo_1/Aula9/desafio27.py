'''
Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''
nome = input('Digite o seu nome completo: ').strip().split()
print('O seu primeiro nome é',nome[0])
print('O ultimo nome é',nome[len(nome)-1])
