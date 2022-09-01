# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input("Informe o preço a receber desconto: "))

desconto = 5
precocomdesconto = preco * (1-(desconto/100))

print(f"R$ {preco} com desconto de {desconto}% é igual a R$ {precocomdesconto:.2f}")
