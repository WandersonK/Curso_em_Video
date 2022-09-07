""" Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

reta1 = float(input("Reta 1: "))
reta2 = float(input("Reta 2: "))
reta3 = float(input("Reta 3: "))

if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    if reta1 == reta2 == reta3:
        print("\033[0;32mForma-se um triângulo\033[m \033[34mEquilátero\033[m")
        
    elif reta1 == reta2 or reta1 == reta3 or reta3 == reta2:
        print("\033[0;32mForma-se um triângulo\033[m \033[34mIsósceles\033[m")
        
    else:
        print("\033[0;32mForma-se um triângulo\033[m \033[34mEscaleno\033[m")
        
else:
    print("\033[0;31mNão se forma um triângulo com as retas.\033[m")
