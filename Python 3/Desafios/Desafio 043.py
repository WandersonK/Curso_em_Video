""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

print("\033[35m{0} CÁLCULO DE IMC {0}\033[m".format('=' * 10))

peso = float(input("Informe seu peso (Kg): "))
altura = float(input("Informe sua altura (metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Seu IMC é de {:.2f}, você está \033[35mabaixo do peso\033[m.".format(imc))
    
elif imc >= 18.5 and imc <= 25:
    print("Seu IMC é de {:.2f}, você está com o \033[32mpeso ideal\033[m.".format(imc))
    
elif imc > 25 and imc <= 30:
    print("Seu IMC é de {:.2f}, você está com \033[33msobrepeso\033[m.".format(imc))
    
elif imc > 30 and imc <= 40:
    print("Seu IMC é de {:.2f}, você está com \033[31mobesidade\033[m.".format(imc))
    
else:
    print("Seu IMC é de {:.2f}, você está com \033[31mobesidade móbida\033[m.".format(imc))
