# OPERADOR LOGICO
# 'and' (E) 'or' (OU) 'not' (NÃO)
# 'and' - TODAS AS CODDIÇÕES PRECISAM SER
# VERDADEIRAS
# SE QUALQUER VALOR DOR CONSIDSERADO FALSO,
# A EXPESSÃO INTEIRA SERÁ AVALIADA NAQUEL VALOR
# SÃO CONSIDERADOS 'falsy' (QUE VC JÁ VIU)
# 0 0 0 '' 'false'
# TAMBEM EXISTE O TIPO 'none' QUE É 
# USADO PARA REPRESENTAR UM NÃO VALOR


entrada = input('entrar[E] sair[S]: ')
senha_digitada = input('Senha: ')
senha_permitida = '123'

if (entrada == 'e' or entrada ==  'E') :
    if(senha_digitada == senha_permitida):
        print('entrou')
    else:
       entrada = 's'
else:
    print('opcao invalida')

if entrada == 's' or entrada == 'S':
    print('saiu')

