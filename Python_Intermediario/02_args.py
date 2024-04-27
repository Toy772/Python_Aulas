# args - argumentos não nomeados
# - *args (empacotamentos e desempacotamento)

# Lembrando desempacotamentos
print('--Lembrando desempacotamentos--'.upper())
x, y, *resto = 1,2,3,4
print(x, y, resto)

# em funcoes
print('--em funçoes--'.upper())
def soma(*args):
    # print(args, type(args))
    result = 0
    
    for i in args:
        result += i
    
    return result

total = soma(1,2,3,4,5,6)
print(total)

# -------------------------
# outro exemplo
print('--outro exemplo--'.upper())
numeros = 1,2,3,4,5,6 
print(numeros)
print(soma(*numeros)) # se passa uma tupla desencadeada *ponteiros