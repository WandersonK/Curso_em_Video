# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Informe o número 1: "))
n2 = int(input("Informe o número 2: "))
n3 = int(input("Informe o número 3: "))

maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2

print("{} é o \033[32mmaior\033[m número.".format(maior))

menor = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2

print("{} é o \033[33mmenor\033[m número.".format(menor))