""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""
from time import sleep

print("\033[0;35m{0} BEM VINDO AO BANCO WK {0}\033[m".format('=' * 10))

print("Vamos precisar de algumas informações para analisar sua solicitação! Vamos lá?")

valor_casa = float(input("\033[32m>\033[m Qual o valor do imóvel desejado? R$ "))
salario = float(input("\033[32m>\033[m Qual o seu salário? R$ "))
anos_pagar = int(input("\033[32m>\033[m Em quantos anos você deseja pagar? "))

print("\n\033[32mEnviando dados...\033[m")
sleep(3)

print("\033[32mPerfeito, aguarde um momento enquanto analisamos sua solicitação...\033[m")
sleep(3)

parcela_mensal = valor_casa / (anos_pagar * 12)
salario30 = salario * 0.3

print("\nPara pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(valor_casa, anos_pagar, parcela_mensal))

if parcela_mensal <= salario30:
    print("\n\033[0;30;42mPARABÉNS!!!\033[m Sua solicitação foi aprovada.")
    print("Suas parcelas mensais durante {} anos, serão de R${:.2f}.".format(anos_pagar, parcela_mensal))
else:
    print("\n\033[0;30;41mReprovado.\033[m Infelizmente não conseguimos aprovar sua solicitação.")
    print("Tente novamente em alguns dias.")
