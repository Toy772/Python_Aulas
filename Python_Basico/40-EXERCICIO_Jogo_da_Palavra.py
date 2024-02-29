# faça um Jogo para o usuario adivinhar qual
# a palavra secreta.
# - Você vai propor uma palavra secreta
# qualquer e vai dar a possibilidade para 
# o usuario digitar apanas uma letra.
# - Quando o usuario digitar uma letra, você
# vai confirir se a letra digitada esta ba plavra secreta
    # - se a letra digitada estiver na 
    # palavra secreta; exiba a letra;
    # - Se letra digitada não estiver na
    # palavra secreta; exiba " _ ".
# faca uma contagem de tentativas do seu usuario

import os

palavra_secreta = 'lembranca'
letras_salvas = ''
show_palavra = '_ _ _ _ _ _ _ _ _'
endgame = False
cont = 0

while not endgame:
    print('JOGO: DESCUBRA A PALAVRA')
    print(f'TENTATIVA: {cont}')

    if '_' not in show_palavra:
        print('FIM DE JOGO')
        print(show_palavra)
        endgame = True
        continue

    print(show_palavra) 
    letras_digitada = input('\nDIGITE UMA LETRA: ')
    cont += 1
    
    if len(letras_digitada)> 1:
        os.system('cls')
        print('DIGITE SOMENTE UMA LETRA:')       
        continue
    
    
    
    show_palavra = ''
    if letras_digitada in palavra_secreta:
        letras_salvas += letras_digitada

    for l in palavra_secreta:
        if l in letras_salvas:
            show_palavra += f'{l} '            
        else:
            show_palavra += '_ '
    
    
    
    if not endgame:
        os.system('cls')
    
    