# REPETIÇÕES 
# while (ENQUANTO)
# EXECUTA UMA AÇÃO ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA
# OPERADORES DE ATRIBUIÇÃO 
#    = += -= *= /= //= **= %= 




contador = 0

while contador <= 100 :
    contador += 1
    if contador == 6 :
        print('PULA UM LOOP DO LACO "continue" -')
        continue
    
    if contador >= 10 and contador <=27 :
        print(' 10-27 - OUTRO EXEMPLO "continue" -')
        continue

    if contador > 40 :
        print('INTERROMPE O LAÇO TODO "break" -')
        break

    print(f'{contador} - EITA')
 

