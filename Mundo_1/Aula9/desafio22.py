'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

nome= str(input('Coloque o seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maíusculas é',nome.upper())
print('Seu nome em minúsculas é',nome.lower())
nome_dividido = nome.split()
print('O seu nome tem ao todo',len(''.join(nome_dividido)),'letras')# posso usar o len(nome)-nome.count('') para ter o mesmo resultado
print('O seu primeiro nome é',nome_dividido[0],'e ele tem',len(nome_dividido[0]),'letras')#nome.find('') faz a mesma coisa : )


