# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

num = float(input("Entre com um número: "))

dobro = num * 2
triplo = num * 3
raiz = sqrt(num)

print(f"Dobro de {num} = {dobro}")
print("Triplo de {} = {}".format(num, triplo))
print(f"Raiz de {num} = {raiz:.2f}")
