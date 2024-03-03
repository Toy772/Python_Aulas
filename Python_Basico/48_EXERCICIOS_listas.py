# faça uma lista de compras com listas
# o usuario dece ter a possibilidade de 
# insirir, apagar e listar valores de sua lista
# Nao permita que o programa quebre com 
# erros de indices inexistentes na lista.

import os
saida = False
lista = ['maca', 'alho', 'oleo', 'laranja' ]

while not saida:
    op = input(f'digite:\n[1]Inserir [2]apagar [3]listar [4]sair: '.upper())

    # previne erro de digitar mais de um caracter
    if len(op)>1:
        print('Digite somente um caracter')
        continue

    # previne erro de o usuario digitar letras ou caracteres especiais
    try:
        op = int(op)
    except:
        print('Digite somente numeros')    

    # Insere o produto na lista
    if op == 1:
        insere = input('Digite o nome do Produto: '.upper())
        lista.append(insere)
        os.system('cls')
        print(f'"{insere}" foi inserido na lista de Produtos'.upper())
    
    # Remove produto da lista
    elif op == 2:
        permited = False
        while not permited: 
            apagar = input('digite o indice a ser apagado: '.upper())
            try:
                apagar = int(apagar)
            except:
                print('Digite somente indice!'.upper())
                continue
            if(apagar > len(lista) or apagar <= 0):
                os.system('cls')           
                print('esse indice nao existe entao nada será apagado!'.upper())
                permited = True
                continue
            os.system('cls')           
            print(f'"{lista[apagar -1]}" foi apagado da lista de produtos!'.upper())
            lista.pop(apagar -1 )
            permited = True
    
    # lista os produtos da lista
    elif op == 3:
        os.system('cls')
        for i in enumerate(lista):
            indice , nome = i             
            print(f'{indice+1} - {nome}'.upper())

    # finaliza o programa
    elif op == 4:
        saida = True
    
    else:
        os.system('cls')
        print('Nao é uma opcao valida\ndigite opções de 1 a 4! '.upper())
        

    

    # os.system('cls')


