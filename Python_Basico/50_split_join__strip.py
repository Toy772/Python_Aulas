# split e join com list e str
# split - divide um string
# join - une uma string

frase = 'Olhe so que - coisa interessante'
lista_palavra = frase.split() # separa por espaço
print(lista_palavra)

lista_palavra = frase.split('-')
print(lista_palavra)

frase_unidas = '-'.join('abc')
print(frase_unidas)

frase_unidas = '***'.join(lista_palavra)
print(frase_unidas)
