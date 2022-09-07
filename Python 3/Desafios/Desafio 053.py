# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print("Digite uma palavra ou frase (sem acentuação) para verificar se ela é um palíndromo:")
frase = input(">> ").upper()

verificar = frase.replace(" ", "")[::-1]

if frase.replace(" ", "") == verificar:
    print(f"{frase} é um palíndromo")

else:
    print(f"{frase} não é um palíndromo")

print(f"Seu inverso é: {verificar}")


"""  Resolução Guanabara  """
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

inverso = junto[::-1]

"""for letra in range(len(junto) + 1, -1, -1):
    inverso += junto[letra]"""

print("O inverso de {} é {}".format(junto, inverso))

if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")