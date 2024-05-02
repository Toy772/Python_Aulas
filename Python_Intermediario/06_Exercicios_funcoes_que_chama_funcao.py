# exercicios
# crie funcoes que duplicam,triplicam e qudruplicam
# o numero recebido como parametro

def multiplica(vlr):
    def mx(mult):
        return vlr * mult
    return mx

n_mult = multiplica(6)

print(f'x2 = {n_mult(2)}')
print(f'x3 = {n_mult(3)}')
print(f'x4 = {n_mult(4)}')