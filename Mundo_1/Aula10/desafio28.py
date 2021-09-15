import random
from time import sleep # ele pausa o programa por um determinado tempo
'''
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número 
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido 
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
n = random.randint(0,5)
print('-=-'*10)
usuario = int(input('Advinhe o número do programa de 1 a 5: '))
print('-=-'*10)
print('Processando...')
sleep(2)
if usuario == n :
    print(f'Você acertou, parabéns, o número que pensei foi o {n} e não o {usuario}')
else:
    print(f'Você errou, tente novamente, o número que pensei foi o {n} e não o {usuario}')
    print('-=-'*10)
