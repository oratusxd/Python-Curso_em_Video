'''a = 5 + 3 * 2
print(a)
b = 3 * 5 + 4 ** 2
print(b)
c = 3 * (5 + 4) ** 2
print(c)
d = 365**522
print (d)
e = 18%2
print(e)
f = 122%3
print(f)
g = 4**3
print(g)
h = pow(4,3) # É um método interno do python para fazer potenciação
print (h)
i = 81**(1/2) # é uma forma de forçar o python a resolver uma raiz
print (i)
j = 127**(1/3)
print(j)
nome = input ('Qual é o seu nome? ')
print(f'Prazer em te conhecer {nome:}')'''
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é tanto {} , o produto é {} e a divisão é {:.3f}'.format(s,m,d), end = '>>>')
print('A divisão inteira {} e a potência {}'.format(di, e))