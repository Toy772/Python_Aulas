# EXERCICO WHILE 

nome = input('DIGITE SEU NOME: ')


length = len(nome)

cont = 0
showName = '*'
while cont < length:
    showName += nome[cont]+'*'
    cont += 1
print('---end---')

print(showName)
print(len(nome))