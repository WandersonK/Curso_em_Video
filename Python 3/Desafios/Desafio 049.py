# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input("Informe um número para tabuada de multiplicação: "))

print(f"\nTabuada do {n}")
for i in range(1, 11):
    print(f'{n} x {i:2} = {n * i}')

print("FIM!")
