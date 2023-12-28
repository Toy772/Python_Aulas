# FORMATAÇÃO BASICA DE STRINGS
# s - strings
# d - int
# f - float
# .<numeros de digitos>f
# x ou X - HEXADECIMAL
# (CARACTERE)(><^)(QUANTIDADE)
# > - ESQUERDA
# < - DIREITA
# ^ - CENTRO
# SINAL - + OU - 
# EX.:  0>-100,.1f
# CONVERSATION FLAGS -!r !s !a


variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:_^10}')
print(f'{1000.04515121513156:,.2f}')
print(f'o hexadecimal de 1500 é {1500:08X}')


