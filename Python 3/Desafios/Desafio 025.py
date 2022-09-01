# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Informe seu nome completo: ")

if "SILVA" in nome.upper():
    print("Possui SILVA no nome")
else:
    print("Não possui SILVA no nome")