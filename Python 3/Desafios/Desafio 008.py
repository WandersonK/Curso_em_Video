# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

num = float(input("Informe a metragem: "))

quilometros = num / 1000
hectometros = num / 100
decametros = num / 10
decimetros = num * 10
centimetros = num * 100
milimetros = num * 1000

print(f"{num} metro em quilômetros = {quilometros}km")
print(f"{num} metro em hectômetros = {hectometros}hm")
print(f"{num} metro em decâmetros = {decametros}dam")
print(f"{num} metro em decimetros = {decimetros:.0f}dm")
print(f"{num} metro em centimetros = {centimetros:.0f}cm")
print(f"{num} metro em milimetros = {milimetros:.0f}mm")
