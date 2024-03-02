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
print(f'{lista} - imprimindo lista'.upper())
print('---------')
# -------------------------------------

lista.clear()
print(f'{lista} - a lista foi limpa'.upper())
print('---------')
# ---------------------------------------

lista = [10,20,30,40]
print(f'{lista} - imprimindo lista'.upper())
lista.insert(2,25)
print(f'{lista} - um novo elemento foi inserido no elemento 2'.upper())

print('---------')