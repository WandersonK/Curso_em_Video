# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostranto os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))

print("\nA PA para os dados informados é: ")

i = 0

while i < 10:
    print(primeiro_termo, end=" -> ")
    primeiro_termo += razao
    
    i += 1

print("FIM")
