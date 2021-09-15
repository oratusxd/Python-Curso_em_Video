from datetime import datetime
'''
Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
usuario = str(input('Coloque um ano aleatório.Digite 0 para analisar o ano atual: ')).strip()
if usuario in '0':
    now = datetime.now()
    usuario = now.year
    if usuario % 4 == 0 and usuario % 100 != 0 and usuario % 400 == 0:
        print(f'{usuario} é BISSEXTO')
    else:
        print(f'{usuario} não é BISSEXTO')
else:
    ano_usuario = int(usuario)
    if ano_usuario % 4 == 0 and ano_usuario % 100 != 0 and usuario % 400 == 0:
        print(f'{ano_usuario} é BISSEXTO')
    else:
        print(f'{ano_usuario} não é BISSEXTO')