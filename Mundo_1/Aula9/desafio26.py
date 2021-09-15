'''
Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas
vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição 
ela aparece a última vez.
'''
frase = ''+str(input('Digite uma frase: ')).strip()# eu podia colocar o upper ou low aqui
print('A letra A aparece',frase.lower().count('a'),'vezes na frase.')
print('A primeira letra A apareceu na posição',frase.lower().find('a')+1) # O +1 serve para contar do 1 em vez de começar da posição 0
print('A ultima letra A apareceu na posição',frase.lower().rfind('a')+1)


