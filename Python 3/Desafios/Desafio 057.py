# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Olá, qual seu sexo [M/F]? ")).upper()

while 'F' != sexo != 'M':
    print("Valor inválido, pfv, informe corretamente:")
    sexo = str(input("[M ou F] >> ")).upper()

print("Fim")
