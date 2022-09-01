# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

reais = float(input("Informe o valor na carteira R$ "))

cotacao_dolar = 3.27

print(f"Com R$ {reais} você pode comprar US$ {(reais / cotacao_dolar):.2f}")