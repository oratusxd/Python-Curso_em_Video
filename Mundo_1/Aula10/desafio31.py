'''
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 
parta viagens mais longas.
'''
print('Bem vindo ao calculador de passagens.')
distancia = str(input('Coloque a distância da sua próxima viagem (km): ')).strip()
distanciakm = float(distancia)
print(f'Você está prestes a começar uma viagem de {distanciakm}km')
if distanciakm <= 200:
    di = distanciakm * 0.50
else:
    di2 = distanciakm * 0.45
    print(f'O preço da sua passagem será de R${di2:.2f}')
    
'''
preco = distancia *0.50 if distancia <=200 else distancia * 0.45

'''
    