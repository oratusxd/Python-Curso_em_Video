frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print('oi')

print('''O meu amor vem da terra e do mar
Uma musa estendida na areia
Anjo de um céu de estrelas do mar
Um balé de mulher e baleia''') #As 3 aspas quebram o texto como aparece no print
print(frase.upper().count('0'))
print(len(frase.strip()))
print(frase.replace('Python','Android')) #eu posso mudar o código, mas não de forma efetiva, pois a string é imutável, agora, se vc atribuir outra variável para essa mudança... a história muda
print(frase)
print('Curso'in frase)
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido[2][3])
