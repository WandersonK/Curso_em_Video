""" Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120
"""

num = 1

fatorial = int(input("Informe um número para fatorial: "))

print(f"{fatorial}! =", end=" ")

while fatorial > 0:
    num *= fatorial
    fatorial -= 1

print(num)
