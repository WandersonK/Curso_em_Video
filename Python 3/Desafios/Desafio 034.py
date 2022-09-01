""" Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input("Informe o salário: "))

if salario > 1250:
    print("Você terá um \033[32maumento\033[m de 10%, totalizando \033[0;30;42mR${:.2f}\033[m".format(salario * 1.1))
else:
    print(f"Você terá um \033[32maumento\033[m de 15%, totalizando \033[0;30;42mR${salario * 1.15:.2f}\033[m")
