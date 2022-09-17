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



"""   Forma do Guanabara   """
núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
