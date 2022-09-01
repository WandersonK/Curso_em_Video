""" Crie um programa que leia o nome completo de uma pessoa e mostre:
-> O nome com todas as letras maiúsculas
-> O nome com todas minúsculas
-> Quantas letras ao todo (sem considerar espaços)
-> Quantas letras tem o primeiro nome
"""

nome_pessoa = str(input("Informe o nome: ")).strip()

print("Analisando seu nome...")
print(f"Seu nome em Maiúsculo é {nome_pessoa.upper()}")
print(f"Seu nome em minúsculo é {nome_pessoa.lower()}")
print(f"Seu nome tem ao todo {len(nome_pessoa) - nome_pessoa.count(' ')} letras.")
print(f"Seu primeiro nome tem {len(nome_pessoa.split()[0])} letras.")
# print("Seu primeiro nome tem {} letras.".format(nome.find(' ')))
