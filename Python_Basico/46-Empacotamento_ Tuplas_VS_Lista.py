# introduçao ao empacotamento + tuples (tuplas)

print('---------EMPACOTAMENTO---------')
nome1, nome2, nome3  = ['Maria','Helena','Luiz']
print(f'{nome1} . {nome2} . {nome2} - variaveis empacotada'.upper())
print('--------')

# -----------

nome1,*resto  = ['Maria','Helena','Luiz']

print(f'{nome1},{resto} - empacota uma variavel e joga o resto em outra lista '.upper())
print('--------')

_ , _ , nome1 , *resto = ['Maria','Helena','Luiz']
print(f'{_} {_} {nome1} {resto} - convensao "_" para itens que nao vai usar '.upper())
print('\n')

# -------------------------------------------------

print('------------TUPLAS--------------')

# -------------
# Tipo de Tupla - uma lista imutavel
# [] é possivel alterar futuramente
# () nao e possivel alterar futurtamente

nomesEX1 = ['Maria','Helena','Luiz']
print(f'{nomesEX1} - é possivel alterar futuramente'.upper())
nomesEX1[0] = 'Joao'
print(f'{nomesEX1} - mudança do primeiro elemento da lista'.upper())
print('--------\n')

nomesEX2 = 'Maria','Helena','Luiz'
print(f'{nomesEX2} - somente leitura\n'.upper())

# É possivel converter tuplas em lista e vise versa

nomesEX2 = list(nomesEX2)  #Conversao para lista
nomesEX1 = tuple(nomesEX1) #Convresao para tuplas

print(f'nomesEX1 era uma lista agora é tuplas - {nomesEX1}'.upper())
print(f'nomesEX2 era uma tupla agora é lista - {nomesEX2}'.upper())




