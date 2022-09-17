""" Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120
"""

"""   Utilizando WHILE   """

num = 1
sequencia = ''

fatorial = int(input("Informe um número para fatorial: "))

print(f"{fatorial}! =", end=" ")

while fatorial > 0:
    num *= fatorial
    
    sequencia += str(fatorial)
    
    if fatorial > 1:
        sequencia += ' x '
        
    fatorial -= 1
    
print(f"{sequencia} = {num}")


"""   Utilizando FOR   """

num = 1
sequencia = ''

fatorial = int(input("Informe um número para fatorial: "))

for i in range(fatorial, 0, -1):
    num = num * i
    sequencia += str(i)
    if i > 1:
        sequencia += ' x '

print(f"{fatorial}! = {sequencia} = {num}")



"""  FORMA DO GUANABARA   """
n = int(input("Digite um número para calcular seu Fatorial: "))
c = n
f = 1
print("Calculando {}! = ".format(n), end="")
while c > 0:
    print("{}".format(c), end="")
    print(" x " if c > 1 else ' = ', end="")
    f *= c
    c -= 1
print("{}".format(f))