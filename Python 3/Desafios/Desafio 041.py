""" A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""

from datetime import date

print("\033[35m{0} VERIFICAR CATEGORIA DE NATAÇÃO {0}\033[m". format('=' * 10))

ano_nascimento = int(input("Informe o seu ano de nascimento para verificar a categoria: "))

idade = date.today().year - ano_nascimento

print("O atleta tem {} anos.".format(idade))

if idade > 0 and idade <= 9:
    print("A categoria para a idade informada é: \033[34mMIRIM\033[m")
elif idade > 9 and idade <= 14:
    print("A categoria para a idade informada é: \033[34mINFANTIL\033[m")
elif idade > 14 and idade <= 19:
    print("A categoria para a idade informada é: \033[34mJUNIOR\033[m")
elif 19 < idade <= 25:
    print("A categoria para a idade informada é: \033[34mSÊNIOR\033[m")
elif idade > 25:
    print("A categoria para a idade informada é: \033[34mMASTER\033[m")
else:
    print("\033[31mA idade informada é inválida, tente novamente!\033[m")
