'''
Desafio 5: Faze um programa que leia um número inteiro e mostre na tela
o seu sucessor e seu antecessor
'''
n = int(input('Coloque um número qualquer: '))
n_antes = n - 1
n_depois = n + 1
print(f'O número escolhido foi {n}, seu o antecessor é {n_antes} e o sucessor é {n_depois}.') 
#Eu posso usar .format(n, (n-1), (n+2)))