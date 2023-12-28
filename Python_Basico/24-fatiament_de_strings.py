# FATIAMENTO DE STRINGS
# 012345678
# OLA MUNDO
# -987654321
# FATIAMENTO [i:f:p] [::]
# OBS.: A FUNÇÃO len RETORNA A QTD
# DE CARACTERES DA str

variavel = 'ola_mundo'


# pedaco de uma string
print('pedaco de uma string:')
print(f'{variavel[4:7]}\n -------')

# apartir de um determinado ponto ate o fim
print('apartir de um determinado ponto ate o fim:')
print(f'{variavel[4:]}\n -------')

# Do inicio ate um determinado ponto
print('Do inicio ate um determinado ponto:')
print(f'{variavel[0:5]}...\n -------')

# mostra uma letra da string
print('mostra uma letra da string:')
print(f'{variavel[5]}\n -------')

# retorna o tamanho da string
print(f'tamnho de variavel = {len(variavel)}')

# passos de variavel
print(f'------\npula em 2 em 2 a variavel\n{variavel[0: len(variavel):2]}')

# VARIAVEL DE TRAS PARA FRENTE
print(f'{variavel[-1:-len(variavel)-1:-1]}')

# variavel[]