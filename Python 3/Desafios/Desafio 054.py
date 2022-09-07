# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

print("Vamos ler 7 anos para verificar a maioridade:")

maiores = []
nao_maiores = []

for i in range(1, 8):
    data = int(input(f"Informe o {i}º ano: "))
    
    if date.today().year - data >= 21:
        maiores.append(data)
    else:
        nao_maiores.append(data)

maiores.sort()
nao_maiores.sort()

print("\033[35mDos anos informados:\033[m")
print(f"> \033[32m{len(maiores)}\033[m são maiores: {maiores}")
print(f"> \033[32m{len(nao_maiores)}\033[m são menores: {nao_maiores}")


"""   Forma Guanabara   """
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input("Em que ano a {}º pessoa nasceu? ".format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print("Ao todo tivemos {} pessoas maiores de idade.".format(totmaior))
print("E também tivemos {} pessoas menores de idade.".format(totmenor))
