"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se
por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import datetime

dados = dict()
ano_atual = datetime.today().year

dados['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = ano_atual - ano_nascimento
dados['ctps'] = int(input('Número da CTPS [Caso não tenha, informe 0]: '))

if dados['ctps'] > 0:
    dados['ano_contatacao'] = int(input('Ano da contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['idade_aposentar'] = (35 - (ano_atual - dados['ano_contatacao'])) + dados['idade']

print('-=' * 30)

for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')


# Forma do Guanabara

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
