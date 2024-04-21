"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

---------------------------------------------------

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0

"""
import re
import sys
import random

# declaracao de variaveis
cpf_user = ''
multi = 10
soma = 0

# Menu de entrda
exit_ = False
while not exit_:
    op = input('[1] Gerar CPF [2] Verificar CPF: ')
    if int(op) is int(1) or int(op) is int(2):
        exit_ = True

# gera CPF
if int(op) == 1:
    for i in range(11):
        cpf_user += str(random.randint(0,9))
else:
    cpf_user = input('DIGITE O CPF: ')
# -----------------------------------------------

cpf_sec = cpf_user == cpf_user[0] * len(cpf_user)

# VERIFICA NUMEROS EM SEQUENCIA
if(cpf_sec):
    print('NUMEROS EM SEQUENCIA NÃO É CPF')
    sys.exit()

# tira os caracteres indesejados
cpf_user = re.sub(r'[^0-9]','',cpf_user)

# ----------------------
cpf_cal = cpf_user[:9]
# --calculo primeiro digito--- 
for i in cpf_cal:    
    soma += int(i) * multi
    multi-=1
# -----------------------

soma = soma* 10
d1 = soma % 11 # d1 - primeiro digito
d1 = d1 if d1 < 10 else 0


# --calculo segundo digito--- 

multi = 11
cpf_cal += str(d1) # - ADCIONA O PRIMEIRO DIGITO PARA O CPF
soma = 0

for i in cpf_cal:    
    soma += int(i) * multi
    multi-=1

soma = soma* 10
d2 = soma % 11 # d1 - primeiro digito
d2 = d2 if d2 < 10 else 0

cpf_cal += str(d2) # ADCIONA O SEGUNDO DIGITO PARA O CPF

# TESTA SE OS CPFS SAO IGUAIS SE FOREM O CPF E VALIDO
if(int(op) == 2):
    if cpf_cal == cpf_user:
        print(f'{cpf_cal} É VALIDO')
    else:
        print(f'{cpf_cal} É INVALIDO')
else:
    print(f'CPF GERADO É {cpf_user}')

