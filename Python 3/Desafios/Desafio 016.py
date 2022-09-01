# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import floor, trunc

num_real = float(input("Informe um número com casa decimal: "))

print(f"O número {num_real} tem a parte inteira {floor(num_real)}")
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num_real, trunc(num_real)))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num_real, int(num_real)))