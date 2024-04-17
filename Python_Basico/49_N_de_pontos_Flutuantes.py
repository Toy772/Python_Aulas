# Imprecisão de ponto flutuante
# Double-precision floating-point format IEEE 754
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2

print(f'metodo 1 \n--------------\n')
print(numero_3)

print(f'metodo 2 \n--------------\n')

print(f'{numero_3:.1f}') # retorna uma str

print(f'metodo 3 \n--------------\n')

print(round(numero_3, 1)) # retorna float

print(f'metodo 4 \n--------------\n')

numero_4 = decimal.Decimal('0.1')
numero_5 = decimal.Decimal('0.7')
numero_6 = numero_4 + numero_5

print(numero_6)


