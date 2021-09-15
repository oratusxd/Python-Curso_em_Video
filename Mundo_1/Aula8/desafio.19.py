import random
'''
Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar 
o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela 
o nome do escolhido.
'''
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

''' Não tem necessidade de fazer isso o que está comentado
res = []
res.append(aluno1)
res.append(aluno2)
res.append(aluno3)
res.append(aluno4)'''
res = [aluno1,aluno2,aluno3,aluno4]
resa= random.choice(res)
print(f'{resa}')