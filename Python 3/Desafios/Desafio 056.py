""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
-> A média de idade do grupo
-> Qual é o nome do homem mais velho
-> Quantas mulheres têm menos de 20 anos.
"""

soma_idades = 0
mais_velho = ''
maior_idade = 0
qtd_mulheres20 = 0

for i in range(1, 5):
    print("\033[33mInforme os dados da {}º pessoa:\033[m".format(i))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M ou F): ")).upper()
    
    soma_idades += idade
    
    if idade > maior_idade and sexo == 'M':
        maior_idade = idade
        mais_velho = nome
    
    if sexo == 'F' and idade < 20:
        qtd_mulheres20 += 1
    
print("\nA média das idades é igual a {:.2f}.".format(soma_idades/4))
print(f"O homem mais velho é o {mais_velho} com {maior_idade} anos.")
print("A quantidade de mulheres com menos de 20 anos é igual a {}.".format(qtd_mulheres20))



"""  Forma do Guanabara   """

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print("----- {}º PESSOA -----".format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print("A média de idade do grupo é de {} anos".format(médiaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))
