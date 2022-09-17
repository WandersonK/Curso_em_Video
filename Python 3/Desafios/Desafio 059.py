""" Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

num1 = int(input("Informe o 1º valor: "))
num2 = int(input("Informe o 2º valor: "))

opcao = 0

while opcao != 5:
    opcao = int(input("""
O que você gostaria de fazer:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
>> """))
    
    if opcao == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    if opcao == 2:
        print(f"{num1} x {num2} = {num1 * num2}")
    if opcao == 3:
        maior = num1 if num1 > num2 else num2
        print(f"O maior valor é {maior}")
    if opcao == 4:
        num1 = int(input("Informe o 1º valor: "))
        num2 = int(input("Informe o 2º valor: "))
    if opcao < 1 or opcao > 5:
        print("Opção Inválida, tente novamente.")

print("FIM")
