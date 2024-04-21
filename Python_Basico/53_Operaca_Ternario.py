# OPERAÇÃO TERNARIO (CONDICAO DE UMA LINHA)
# <valor> if <condicao> else <outro valor>


print('VALOR' if True else 'OUTRO VALOR') 

print('----------')

condicao  = 10 == 11
var = 'VALOR' if condicao else 'OUTRO VALOR'
print(var)

print('--------')

digito = input('DIGITE UM NUMERO : ')
digito = int(digito)
novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito

print(f'O NOVO DIGITO É {novo_digito}')