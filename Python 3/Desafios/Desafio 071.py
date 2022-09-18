""" Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor será entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
"""

divisor = '=' * 30

print(divisor)
print('{:^30}'.format("BANCO WK"))
print(divisor)

qtd_sacar = int(input("Favor, informe a quantidade para sacar: R$ "))

notas50 = qtd_sacar // 50
qtd_sacar = qtd_sacar - (notas50 * 50)

notas20 = qtd_sacar // 20
qtd_sacar = qtd_sacar - (notas20 * 20)

notas10 = qtd_sacar // 10
qtd_sacar = qtd_sacar - (notas10 * 10)

notas1 = qtd_sacar // 1

print("Você receberá:")

if notas50 != 0:
    print(f"Total de cédulas de R$ 50: {notas50}")
if notas20 != 0:
    print(f"Total de cédulas de R$ 20: {notas20}")
if notas10 != 0:
    print(f"Total de cédulas de R$ 10: {notas10}")
if notas1 != 0:
    print(f"Total de cédulas de R$  1: {notas1}")

print(divisor)
print("Obrigado pela Preferência! Volte Sempre!")



""" FORMA GUANABARA  """

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
