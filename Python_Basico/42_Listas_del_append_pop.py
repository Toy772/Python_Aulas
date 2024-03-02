# Listas em python
# Tipo de listas - Mutavel
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - indices e fatiamentos
# metodos úteis: 
#       append - adiciona um elemento no final da lista (METODO)
#       insert - adiciona um elemento no indice escolhido da lista (METODO)
#       pop - apaga um elemento do final ou do indice escolhido da lista (METODO) 
#       del - apaga um elemento da lista
#       clear - apaga todos os elementos da lista (METODO)
#       extend -estende a lista (METODO)

# -----------CRUD---------------
#       create - criar
#       Read - ler
#       update - alterar
#       delete - apagar  



# -------------Listas-------------------
lista = [10,20,30,40]
print(f'{lista} - imprime a lista inteira'.upper()) # imprime a lista inteira
print('-----')

del lista[2]  # apaga o indice 2
print(f'{lista} - indice 2 apagado'.upper()) # idice 2 apagado
print('-----')

print(f'{lista[2]} - imprime item do indice 2'.upper()) # 
print('-----')

lista.append(50) # novo indice adicionado
lista.append(60) # novo indice adicionado
lista.append(70) # novo indice adicionado
print(f'{lista} - novos indice adicionado ao final da lista'.upper())
print('-----')
lista.pop() # remove o ultimo indice da lista
print(f'{lista} - ultimo indice da lista removido'.upper())
print('-----')
removido = lista.pop(3) # remove o indice 3 da lista
print(f'{lista} - o indice 3 foi removido da lista'.upper(), f'--{removido}-- removido'.upper())


# -------------------------------------------

