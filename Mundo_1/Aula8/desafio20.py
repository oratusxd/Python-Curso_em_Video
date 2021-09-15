'''
Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a 
ordem sorteada.
'''
import random
nome1 = input('Coloque o primeiro aluno: ')
nome2 = input('Coloque o segundo aluno: ')
nome3 = input('Coloque o terceiro aluno: ')
nome4 = input('Coloque o quarto aluno: ')
lista_nome = [nome1,nome2,nome3,nome4]
res = (random.sample(lista_nome,len(lista_nome)))
print('A ordem de apresentação será: ')
print(res)