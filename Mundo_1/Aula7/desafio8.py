'''
Escreva um programa que leia valor em metros e exiba convetido em centímetros
e em milímetros
'''
metro = float (input('Coloque o valor em metros: '))
km = metro/1000
hm = metro/100
dam = metro/10
dm = metro*10
cm = metro*100
mm = metro*1000
print(f'{metro} metros medirá:\n{km}km, {hm} hm , {dam} dam\n{dm} dm, {cm} cm e {mm} mm')

 