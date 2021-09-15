'''
 Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário,
 ,com 15 porcento de aumento
'''
salario = float(input('Coloque o seu salário atual: '))
aumentoo = 15
aumento1 = float((salario*aumentoo)/100)
novo_salario = float(salario + aumento1)
print(f' O seu novo salário é de R${novo_salario:.2f}')
