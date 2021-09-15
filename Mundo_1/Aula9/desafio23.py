'''
Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na 
tela cada um dos dígitos separados.
'''
numero = int(input('Informe um número: '))

print(f'Analisando o número {numero}')
u = numero // 1 % 10
d = numero // 10 % 10
c = numero //100 % 10
m = numero // 1000 % 10
print('Unidade: ',u)
print('Dezena: ',d)
print('Centena: ',c)
print('Milhar: ',m)
# Esse eu precisei ver o resultado, porque tava tenso