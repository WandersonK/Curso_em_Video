# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

digitado = input("Entre com algo para análise: ")

print("O tipo primitivo desse valor é {}".format(type(digitado)))
print("Só tem espaços? {}".format(digitado.isspace()))
print("É um número? {}".format(digitado.isnumeric()))
print(f"É alfabético? {digitado.isalpha()}")
print(f"É alfanumérico? {digitado.isalnum()}")
print("Está em maiúsculas?", digitado.isupper())
print("Está em minúscula?", digitado.islower())
print("Está capitalizada?", digitado.istitle())
