'''
Exercício Python 34: Escreva um programa que pergunte o salário de um 
funcionário e calcule o valor do seu aumento. Para salários superiores a 
R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento 
é de 15%.
'''
salario = float (input('Qual é o salário do funcionário? '))
if salario > 1250:
    res = salario +(salario *10)/100
else:
    res = salario +(salario *15)/100
print(f'Quem ganhava R${salario:.2f} passa a ganha R${res:.2f} agora')
    