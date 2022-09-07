# Faça um programa que leia um número inteiro e diga se ele é ou não um primo.

num_teste = int(input("Informe um número inteiro: "))

countdivisiveis = 0

for i in range(1, num_teste + 1):
    if num_teste % i == 0:
        countdivisiveis += 1


if countdivisiveis == 2:
    print(f"{num_teste} É um número Primo.")
else:
    print('{} Não é um número Primo.'.format(num_teste))
