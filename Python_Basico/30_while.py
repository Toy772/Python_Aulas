# REPETIÇÕES 
# while (ENQUANTO)
# EXECUTA UMA AÇÃO ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA
# OPERADORES DE ATRIBUIÇÃO 
#    = += -= *= /= //= **= %= 


condicao = True
print('DIGITE "S" PARA SAIR ')
while condicao < 3:
    nome = input('Qual seu nome ')
    print(f'Seu nome e {nome}')
    
    if nome == 'S' or nome == 's':
        break

print('Acabou')


#   ---

contador = 0

while contador < 10 :
    print(f'{contador + 1} - LOUA')
    contador += 1

#  ------