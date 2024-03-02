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
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b

print(f'{lista_c} - lista concatenada'.upper())
print('----------')

# ---------------------------------------------------

lista_a.extend(lista_b)
print(f'{lista_a} - lista extendida - lista A recebeu lista B'.upper())
print('----------')

# -----------------------------------------------------




