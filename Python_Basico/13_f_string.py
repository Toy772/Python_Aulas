nome = "vagner O Roxo"
altura = 1.80
peso = 95
imc = ...

imc = 95 /(altura**2 )
# vagner o roxo tem 1.80 de altura
# pesa 95 quilos e seu IMC é 
# 29.320987654320987

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'e pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)