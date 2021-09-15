'''
Exercício Python 16: Crie um programa que leia um 
número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''

'''from math import floor, trunc
num = float(input('Coloque um número aleatório: '))
res = trunc(num) 
trunc arredonda para cima ou para baixo em direção a zero, já o .floor arredonda para o 
infinito negativo, ou seja, para números positivos ele dá o mesmo resultado que o trunc, 
já em negativos a situação muda
print(f'O número {num} e a sua porção inteira é {res}')'''

#resolução alternativa;
num = float(input('Coloque um número: '))
res = int(num)
print(f'O número {num} e a sua porção inteira é {res}')