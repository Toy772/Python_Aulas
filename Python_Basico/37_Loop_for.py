texto = 'Python'
novo_texto = ''

for l in texto:
    novo_texto += f'*{l}'
    print(l)

print(novo_texto + '*')

print('---------------------')


# -----------------------------------------------------

# For + Range
# range -> range(start,stop,step)
# range -> range(stop)
# ----------------------------------------------------

numbers = range(0, 32 ,2)
for nro in numbers:
    print(nro)