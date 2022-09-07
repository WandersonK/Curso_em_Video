# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print("Verificar pesos:")

pesos = []

for i in range(1, 6):
    pesos.append(float(input(f"Informe o {i}º peso: ")))
    
pesos.sort()

print(f"O \033[32mmenor\033[m peso é o {pesos[0]}Kg")
print(f"O \033[32mmaior\033[m peso é o {pesos[-1]}Kg")



"""   Forma do Guanabara   """
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {}Kg".format(maior))
print("O menor peso lido foi de {}Kg".format(menor))
