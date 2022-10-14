"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

lista_total = [[], []]

for i in range(0, 7):
    num = int(input(f'Digite o {i + 1}º valor: '))

    if num % 2 == 0:
        lista_total[0].append(num)
    else:
        lista_total[1].append(num)
        
print(f'Os números pares digitados foram {sorted(lista_total[0])}')
print(f'Os números ímpares digitados foram {sorted(lista_total[1])}')


# Forma do Guanabara

núm = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')
