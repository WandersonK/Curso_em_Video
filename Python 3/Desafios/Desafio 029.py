""" Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
"""

velocidade = int(input("Informe a velocidade do carro: "))

if velocidade > 80:
    print("\033[1;31mVocê ultrapassou o limite de velocidade!\033[m")
    print("A \033[0;41mmulta\033[m será de \033[4mR${:.2f}\033[m.".format((velocidade - 80) * 7))
else:
    print("\033[32mVocê se manteve na velocidade da via!\033[m")
