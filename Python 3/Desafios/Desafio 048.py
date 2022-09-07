# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
count = 0

for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        s += i
        count += 1

print("O somatório dos {} números ímpares e múltiplos de 3 no intervalo de 1 a 500, é igual a: {}".format(count, s))

"""  FORMA 2  """
s = 0
count = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
        count += 1

print("O somatório dos {} números ímpares e múltiplos de 3 no intervalo de 1 a 500, é igual a: {}".format(count, s))
