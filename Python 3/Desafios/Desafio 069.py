""" Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""

todoscadastros = 0
mais18 = 0
homenscadastrados = 0
mulheresmenor20 = 0
divisor = '-' * 30

while True:
    print(divisor)
    print('{:^30}'.format("CADASTRE UMA PESSOA"))
    print(divisor)
    
    idade = int(input("Informe a idade: "))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Informe o sexo: [M/F] ")).strip().upper()[0]

    print(divisor)
    
    todoscadastros += 1
    
    if idade > 18:
        mais18 += 1
    
    if sexo == 'M':
        homenscadastrados += 1
    
    if sexo == 'F' and idade < 20:
        mulheresmenor20 += 1
    
    while True:
        continuar = input("Deseja continuar? [S/N] ").upper()[0]
        if continuar in 'SN':
            break
        
    if continuar == 'N':
        break
    
print("\n{0} FIM DO PROGRAMA {0}".format('=' * 7))
print(f"TOTAL DE CADASTROS: {todoscadastros}.")
print(f"Destes, {mais18} possuem idade supeior a 18.")
print(f"{homenscadastrados} são homens.")
print(f"{mulheresmenor20} são mulheres com idade menor que 20.")
