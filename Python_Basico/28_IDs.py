# flags (BANDEIRAS) - MARCAR UM LOCAL
# none = SEM VALOR
# is E is not = É OU NÃO É (TIPO, VALOR, IDENTIDADE)
# id = IDENTIDADE 

v1 = 'a'
v2 = 'a'
v3 = 'b'
print(id(v1))
print(id(v2))
print(id(v3))
print('-----------------------')

condicao = False
passo_no_if = None


if condicao:
    passo_no_if = True
    print('faça algo')
else:
    print('Não faça algo')


print(f'passou no if ? =  {passo_no_if}...{passo_no_if is None}')
print(f'passou no if ? =  {passo_no_if}...{passo_no_if is not None}')

