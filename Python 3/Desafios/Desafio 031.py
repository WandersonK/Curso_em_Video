# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia_viagem = float(input("Informe a distância da viagem em Km: "))

if distancia_viagem <= 200:
    print("O valor da passagem será de R${}.".format(distancia_viagem * 0.5))
else:
    print("O valor da passagem será de R${}.".format(distancia_viagem * 0.45))
