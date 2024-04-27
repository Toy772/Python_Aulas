"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

def minha_funcao():
    print('Bah varias')
# ---------------------------
def soma(a , b ):
    r = a+b
    desc = f'{a=} + {b=} = {r=}'# mostra nome da varivavel e seu valor na tela
    return desc
# --------------------------
def saudacao(nome='desconhecido'):# para colocar um valor padrao qnd nao e passado nda por parametro
    print(f'Olá {nome}! ')

# -------------------------

# cahmada da funcao
minha_funcao()

# ********

# outros exemplos
saudacao('Vagner')
saudacao('Estranho')
saudacao()

# *************

# funcao com retorno

resposta =  soma(20,10)
print(resposta)
resposta = soma(b=25 , a= 20)#parametros nomeados podendo inverter a ordem dos argumentos
print(resposta)


