# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Informe o salário R$ "))

aumento = 15
salariocomaumento = salario * (1+(aumento/100))

print(f"R$ {salario} com aumento de {aumento}% é igual a R$ {salariocomaumento:.2f}")
