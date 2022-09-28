""" Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

num_aleatorios = []

for i in range(0, 5):
    num_aleatorios.append(randint(0, 10))

num_aleatorios = tuple(num_aleatorios)

print("Os valores sorteados foram: ", end="")

for i in num_aleatorios:
    print(i, end=" ")

print(f"\nO maior valor sorteador foi {max(num_aleatorios)}")
print(f'O menor valor sorteador foi {min(num_aleatorios)}')
