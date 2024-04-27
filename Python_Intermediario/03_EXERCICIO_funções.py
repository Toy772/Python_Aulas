# exercicos com funcoes
# nao nomeados reexibidos
# retorne o total para a variavel e mostre  o valor
# da variavel

# crie uma função que retorne se um valor e par ou impar


def multiplica(*args):
    result = 1
    for i in args:
        result *= i 
    
    return result


def isPar(vlr):
    aux = vlr % 2 == 0
    return aux

# declaracao variaveis

vlr = []
qntNumbMult = ''

# -----------------

qntNumbMult = input('Digite a quantidade denumeros a serem multiplicados: '.upper())
qntNumbMult = int(qntNumbMult)

for i in range(qntNumbMult):
    aux =  input(f'Digite {i+1}º valor: '.upper())
    vlr.append(int(aux))

vlr = tuple(vlr)
r = multiplica(*vlr)


if isPar(r):
    print(f'o vlr {r} é par'.upper())
else:
    print(f'o vlr {r} é ímpar'.upper())