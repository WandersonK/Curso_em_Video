# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

# hipotenusa = (co ** 2 + ca ** 2) ** (1/2)

cateto_oposto = float(input("Entre com o cateto oposto: "))
cateto_adjacente = float(input("Entre com o cateto adjacente: "))

print("A hipotenusa é igual a {:.2f}".format(hypot(cateto_oposto, cateto_adjacente)))
