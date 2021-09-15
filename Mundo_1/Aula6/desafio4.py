'''
Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre 
na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''
dado = input('Coloque um dado qualquer: ')
print('Só tem espaços?',dado.isspace());
print('É um número? ',dado.isnumeric());
print('É alfabético? ',dado.isalpha());
print('É alfanumérico? ', dado.isalnum());
print('Está em letra maíuscula?',dado.isupper());
print('Está em letra minúscula?',dado.islower());
print('Está capitalizada? ', dado.istitle()) # Ele verifica se a palavra tem uma letra maiúscula. tipo Python

