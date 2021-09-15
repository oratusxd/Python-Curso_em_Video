'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos Doláres ela pode comprar
'''
dinheiro = float(input('Quanto de dinheiro que você possui na sua carteira? '))
dolar = 3.27
convert = (dinheiro/dolar)
print(f'Você poderá comprar {convert:.2f} dólares')