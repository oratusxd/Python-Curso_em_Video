'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
'''
numerop = float(input('Coloque um número qualquer: '))
dobro = numerop * 2
triplo = numerop * 3
raiz = numerop**(1/2) # pow(numerop,(1/2)) pode ser uma opção
print(f'O número escolhido foi {numerop}.\nO dobro do número escolhido tem o valor de {dobro}.\nO triplo {triplo}.\nA raiz {raiz:.2f}')