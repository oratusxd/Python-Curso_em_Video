'''
Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa 
ou não com o nome “SANTO”.
'''
cidade = input ('Digite a cidade em que você nasceu: ').strip()
cidade_mi = cidade.lower()
print('santo' in cidade_mi)
#print(cidade[:5].upper() == 'SANTO')-> Foi a solução do professor