# closure e funcoes que retornam outras funcoes

def criar_saudacao(saudacao):
    def saudar(nome):  
        return f'{saudacao},{nome}!'
    return saudar

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa Noite')

for nome in ['Vagner','Alexia','Akane']:
    print(s1(nome))