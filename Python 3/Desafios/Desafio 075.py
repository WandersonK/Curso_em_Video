"""Desenvolva um programa que leia quatro valores pelo teclado e guarade-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

lista_digitados = []

for i in range(1, 5):
    lista_digitados.append(int(input(f"Informe o {i}º número (0 a 10): ")))

lista_digitados = tuple(lista_digitados)

print(f'Você digitou os valores {lista_digitados}')
print(f'O número 9 aparece {lista_digitados.count(9)} vezes.')

if 3 in lista_digitados:
    print(f'O número 3 aparece na {lista_digitados.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os números pares digitados foram: ', end="")

for i in lista_digitados:
    if i % 2 == 0:
        print(i, end=" ")

print()
