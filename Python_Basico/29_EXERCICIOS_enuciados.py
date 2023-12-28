# FACA UM PROGRAMA QUE PEÇA AO USUARIO DIGITAR UM NUMERO INTEIRO
# INFORME SE ESTE NUMERO E PAR OU IMPAR. CASO O USUARIO NAO DIGITE UM NUMERO 
# INTEIRO, INFORME QUE NAO E UM NUMERO INTEIRO
print('--------------------')


number = input('digite um numero real: ')

try:
    number = int(number)

    if number % 2 == 0:
        print(f'o numero {number} é par')
    else:
        print(f'o numero {number} é impar')

except:
    print('Esse caracter nao é um numero real!')



# FACA UM PROGRAMA QUE PERGUNTE A HORA AO USUARIO E, SE BASIANDO-SE NO HORARIO
# DESCRITO, EXIBA A SAUDACAO APROPRIADA. EX
# BOM DIA 0-11 , BOA TARDE 12-17 E BOA NOITE 18-23
print('--------------------')

hora = input('Hora: ')
minuto = input('Minuto: ')

try:
    hora = int(hora)
    minuto = int(minuto)
    
    if hora >= 24 or minuto >= 60 or hora < 0:
        hora = 'a'
        hora = int(hora)
    
    manha = hora >= 0 and hora < 12
    tarde = hora >= 12 and hora < 18    
    
    if manha:
        print(f'Bom dia {hora}-{minuto} ')
    elif tarde:
        print(f'Boa tarde {hora}-{minuto} ')
    else:
        print(f'Boa Noite {hora}-{minuto} ')
                
except:
    print('voce digitou valores invalidos')


# FACA UM PROGRAMA QUE PECA O PRIMEIRO NOME DO USUARIO. SE O NOME TIVER 4 LETRAS OU
# MENOS ESCREVA " SEU NOME E CURTO"; SE TIVER ENTRE 5 E 6 LETRAS, ESCREVA 
# "SEU NOME É NORMAL"; MAIOR QUE 6 ESCREVA "SEU NOME E MUITO GRANDE" 


print('--------------------')

nome = input('SEU NOME: ')
tam = len(nome)

if(tam <=4 ):
    print('seu nome é curto !')
elif(tam >=5 and tam < 7):
    print('seu nome é Normal !')
else:
    print('seu nome é grande !')

print('--------------------')
