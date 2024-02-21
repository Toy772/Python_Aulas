# Interavel -> str, rang, etc (__inter__)
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o proximo valor 
# iter -> me entregue seu iterador

print('----------------')


text = iter('Pessoa')   # .__iter__()

print(next(text)) # .__next__())
print(next(text)) # .__next__())
print(next(text)) # .__next__())
print(next(text)) # .__next__())
print(next(text)) # .__next__())
print(next(text)) # .__next__())

print('----------------')

text2 = 'pessoa2'
inte =  iter(text2)

while True:
    try:
        l = next(inte)
        print(l)
    except StopIteration:
        break


print('----------------')


