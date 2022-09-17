# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))

print("\nA PA para os dados informados é: ")

for i in range(0, 10):
    print(primeiro_termo, end=' -> ')
    primeiro_termo += razao
print("FIM")


""" FORMA GUANABARA """

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razao, razão):
    print('{} '. format(c), end='-> ')
print('ACABOU')
