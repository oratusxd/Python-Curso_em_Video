'''
Exercício Python 002: Faça um programa que leia o nome de uma pessoa 
e mostre uma mensagem de boas-vindas.
'''
nome = input('Digite o seu nome: ')
#print('É um prazer te conhecer,',nome,'!') 
print('É um prazer te conhecer, {}!'.format(nome))
# As duas formas funcionam bem 