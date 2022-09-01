# Faça um programa que leia um Ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input("Informe um ângulo para calculo: "))

print(f"Seno: {sin(radians(angulo)):.2f} "
      f"\nCosseno: {cos(radians(angulo)):.2f} "
      f"\nTangente: {tan(radians(angulo)):.2f}")
