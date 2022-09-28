# lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim' # No Python pode-se criar uma tupla sem informar os Parênteses
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[:2])
print(lanche[-2:])

for comida in lanche:
    print(f"Eu vou comer {comida}")

print("Comi pra caramba!")

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print("Comi pra caramba!")

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('Comi pra caramba!')


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(2))
print(c.index(5))
print(c.index(5, 1))


pessoa = ('Wanderson', 25, 'M', 55)
del(pessoa)
print(pessoa)
