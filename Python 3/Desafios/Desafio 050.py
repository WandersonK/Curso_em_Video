# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar desconsidere-o.

print("Vammos ler 6 números:")

s = 0

for i in range(1, 7):
    n = int(input("Digite o {}º valor: ".format(i)))
    if n % 2 == 0:
        s += n

print("O somatório dos números pares digitados é igual a: {}".format(s))
