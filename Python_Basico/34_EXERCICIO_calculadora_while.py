#   CALCULADORA COM WHILE
import os

while True:
    n1 = input('PRIMEIRO VALOR: ')
    n2 = input('SEGUNDO VALOR: ')
    operador = input('escolha o operador [. * . / . + . - .]: ')

    try:
        n1 = float(n1)
        n2 = float(n2)
        valorpermitido = False
    except:
        valorpermitido  = True       
    
    operadores_permitidos = '+-/*'

    if valorpermitido:
        os.system('cls')
        print('DIGITE UM VALOR VALIDO')
        continue
    
    if len(operador)>1:
        os.system('cls')
        print('DIGITE APENAS UM OPERADOR')      
        continue

    if operador not in operadores_permitidos:
        os.system('cls')
        print('DIGITE UM OPERADOR VALIDO')        
        continue

    if operador == '*':
        soma = n1*n2
    elif operador == '/':
        soma = n1 / n2
    elif operador == '+':
        soma = n1+n2
    else:
        soma = n1 - n2

    print(f'RESULTADO É {soma}')


    sair = input('SAIR [S]').lower().startswith('s')
    os.system('cls')
    if sair:
        break