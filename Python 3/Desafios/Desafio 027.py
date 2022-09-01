# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = str(input("Informe o nome completo: ")).strip()

print(f"primeiro = {nome_completo.split()[0]}")
print(f"último = {nome_completo.split()[-1]}")

