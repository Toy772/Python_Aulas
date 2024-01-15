string = 'valor qualquer'

i=0

while i < len(string):
    letra = string[i]

    # break
    # qnd break e chamdo o else nao e executado
    
    print(letra)
    i += 1
else:
    print('bloco executado')
print('fora do else')