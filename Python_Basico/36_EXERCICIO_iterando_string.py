frase = 'o python é uma linguagem de programação '\
        'multiparadigma' \
        'python foi criado por Guido van Rossum'

qtd_letra_mais_vezes = 0
letra_mais_vezes = ''

i = 0
while i <len(frase):
    la = frase[i]
    
    
    if la == ' ':
        i += 1
        continue

    qtd_letra_atual = frase.count(la)
    
    if qtd_letra_mais_vezes < qtd_letra_atual:
        qtd_letra_mais_vezes = qtd_letra_atual
        letra_mais_vezes = la
    i += 1
   
else:
    print(f'{letra_mais_vezes} {qtd_letra_mais_vezes}x')