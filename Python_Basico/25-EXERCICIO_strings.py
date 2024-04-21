# EXERCICIO
# PEÇA AO USUARIO DIGITAR SEU NOME
# PECA AO USUARIO DIGITAR SUA IDADE 
# SE O NOME E AIDEDE FOREM DIGITADOS
#   EXIBA:
#       SEU NOME É {NOME}
#       SEU NOME INVERTIDO É {NOME INVERTIDO}
#       SEU NOME CONTEM (OU NÃO) ESPAÇOS
#       SEU NOME TEM {n} LETRAS
#       APRIMERA LETRA DO SEU NOME É {letra}
#       A ULTIMA LETRA DO SEU NOME É {letra}
# SE NADA FOR DIGITADO EM NOME OU IDADE:
#   EXIBA 'DESCULPE, VOCE DEIXOU CAMPOS VAZIOS'


nome = input('DIGITE O SEU NOME: ')
idade = input('DIGITE A SUA IDADE: ')

if not nome and idade:
    print('DESCULPE, VOCE DEIXOU CAMPOS VAZIOS')
else: 
    print(f'SEU NOME É {nome}')
    print(f'SEU NOME INVERTIDO É {nome[::-1]}')
    if (' ' in nome):
        print('SEU NOME CONTEM ESPAÇOS')
    else:
        print('SEU NOME NAO CONTEM ESPAÇOS')
    print(f'SEU NOME TEM {len(nome)} LETRAS')
    print(f'A PRIMEIRA LETRA DO SEU NOME É {nome[0]}')
    print(f'A ULTIMA LETRA DO SEU NOME É {nome[-1]}')
        
