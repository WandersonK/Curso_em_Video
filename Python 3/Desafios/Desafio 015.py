# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias_alugados = int(input("Quantos dias alugados? "))
km_percorrido = int(input("Quantos quilômetros percorridos? "))

aluguel_carro = 60 * dias_alugados
gasolina = 0.15 * km_percorrido

print(f"O valor total gasto, foi de R${aluguel_carro + gasolina}")