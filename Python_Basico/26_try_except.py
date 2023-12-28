# INTRODUÇÃO AO try/except
# try -> TENTAR EXECUTAR O CODIGO
# except -> OCORREU ALGUM ERRO AO TENTAR EXECUTAR
import os

numero = input('numero: ')

# print(f'dobro do numero e {numero * 2:.2f}')#casa decimais

try:
    print(f'STR -> {numero} ')
    numero_float = float(numero)
    print(f'FLOAT -> {numero_float}')
    print(f'o dobro de {numero} é {numero_float * 2:.2f}')
except:
    os.system('cls')
    print('Isso não é um numero')