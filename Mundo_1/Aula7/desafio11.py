'''
Crie um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pinta-la. 
Sabendo que para cada 1l de tinta, pinta uma área de 2m²
'''
largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
area = altura * largura
tinta = area / 2
print(f'A área a ser pintada é de {area} m², precisando de {tinta:.2f} litros de tinta.')