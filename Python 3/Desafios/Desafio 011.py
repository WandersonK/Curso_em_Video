# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura_parede = float(input("Informe a largura da parede em metros: "))
altura_parede = float(input("Informe a altura da parede em metros: "))

area_parede = largura_parede * altura_parede
litros_necessarios = area_parede / 2

print(f"São necessários {litros_necessarios} litros de tinta para pintar uma área de {area_parede}m².")