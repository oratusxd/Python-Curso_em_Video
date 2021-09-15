'''
 Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço,
 com 5 porcento de desconto
'''
preco = float(input('Coloque o preço atual do produto: '))
desconto = 5
desconto1 = float((preco*5)/100)
novo_preco = float(preco - desconto1)
print(f' O preço promocional é de R${novo_preco:.2f}')
