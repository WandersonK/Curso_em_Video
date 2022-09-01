# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input("Informe um ano para conferir, ou digite 0 para o ano atual: "))

if ano == 0:
    ano = date.today().year

if ano % 400 == 0 or ano % 100 != 0 and ano % 4 == 0:
    print("O ano {} é Bissexto.".format(ano))
else:
    print("O ano {} não é Bissexto.".format(ano))
