""" Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

num1 = int(input("Insira o \033[33m1º\033[m valor: "))
num2 = int(input("Insira o \033[33m2º\033[m valor: "))

if num1 > num2:
    print("O \033[35mprimeiro\033[m valor é maior.")
elif num2 > num1:
    print("O \033[35msegundo\033[m valor é maior.")
else:
    print("\033[31mNão existe valor maior\033[m, os dois são iguais.")
