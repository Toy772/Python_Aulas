# DESENPACOTAMENTO EM CHAMADAS
# DE METODOS E FUNÇOES

string = 'ABCD'
lista = ['Maria','Helena',1,2,3,'Eduarda']
tupla = 'Python','é','Legal'

p,b, *_, ap , u = lista #'*_' -> pega o resto da lista
print(p,u,ap)

print('---')

for i in lista:
    print(i)

# ou
print('--OU--')

print(*lista, sep='\n')

print('---')