# enumerate - enumera iteravei (indices)


lista = ['Maria','Helena','Luiz']
lista.append('Joao')
for item in enumerate(lista):
    indice, nome = item #desempacotamento
    print(f'{indice} - {nome} ')
