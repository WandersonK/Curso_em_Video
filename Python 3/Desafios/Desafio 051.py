# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))

print("\nA PA para os dados informados é: ")

for i in range(0, 10):
    print(primeiro_termo)
    primeiro_termo += razao
