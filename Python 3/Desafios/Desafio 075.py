"""Desenvolva um programa que leia quatro valores pelo teclado e guarade-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

lista_digitados = []
cont_pares = 0

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
        cont_pares += 1

if cont_pares == 0:
    print("Nenhum!")

print()


#  Forma do Guanabara

núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
