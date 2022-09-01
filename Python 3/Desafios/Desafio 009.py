# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

num = int(input("Entre com um número: "))
i = 1

print('-' * 12)

for i in range(1, 11):
    print(f"{num} x {i:2} = {num * i}")

print('-' * 12)