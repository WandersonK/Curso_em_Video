# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input("Reta 1: "))
reta2 = float(input("Reta 2: "))
reta3 = float(input("Reta 3: "))

if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    print("\033[0;32mForma-se um triângulo com as retas.\033[m")
else:
    print("\033[0;31mNão se forma um triângulo com as retas.\033[m")
