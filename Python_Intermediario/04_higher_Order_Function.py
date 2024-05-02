# Higher Order Function
# Funções de primeira Classe

def saudacao(msg):
    return msg

def saudacao2(msg,nome):
    return f'{msg}, {nome}!'

def executa(fx,msg): # uma funcao que execulta outra funcao
    return fx(msg)

def exec2(fx, *args):# uma funcao que execulta outra funcao - com empacotamento
    return fx(*args)

# -----------------------------------------


v = executa(saudacao,'Boa Noite')

print(v)

print('-------')

print(saudacao2('Bom dia','Vagner'))

print(saudacao2('Bom dia','Ana'))

