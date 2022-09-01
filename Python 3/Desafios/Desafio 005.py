# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

numint = int(input("Entre com um número: "))

antecessor = numint - 1
sucessor = numint + 1

print(f"O antecessor do número {numint} é {antecessor}.")
print(f"O sucessor do número {numint} é {sucessor}.")