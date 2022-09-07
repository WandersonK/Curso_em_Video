""" Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""

from time import sleep

print("\033[35m{0} Convertendo base de números {0}\033[m".format('=' * 10))

num_convert = int(input("Para comerçar, informe o número que deseja converter: "))
num_save = num_convert

print("Agora, indique para qual base deseja que seja convertido:")

print("\033[33m>\033[m \033[1;34m1\033[m para \033[33mBinário\033[m.")
print("\033[33m>\033[m \033[1;34m2\033[m para \033[33mOctal\033[m.")
print("\033[33m>\033[m \033[1;34m3\033[m para \033[33mHexadecimal\033[m.")

escolha_converter = int(input('\033[32m>>\033[m '))


def calculando(base_escolhida, num_convert):
    sleep(0.5)
    print("\n\033[32mCalculando...\033[m")
    sleep(2)
    
    dado_final = ''
    
    while num_convert > 0:
        dado_final = str(num_convert % base_escolhida) + dado_final
        num_convert = num_convert // base_escolhida
        
    return dado_final


if escolha_converter == 1:
    binario = calculando(2, num_convert)
    
    print("\n\033[36m< {} convertido para base 2 (binário), é igual a: {} >\033[m".format(num_save, binario))

elif escolha_converter == 2:
    octal = calculando(8, num_convert)
    
    print("\n\033[36m< {} convertido para base 8 (octal), é igual a: {} >\033[m".format(num_save, octal))

elif escolha_converter == 3:
    tabela_hexa = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }
    
    sleep(0.5)
    print("\n\033[32mCalculando...\033[m")
    sleep(2)
    
    hexadecimal = ''
    
    while num_convert > 0:
        if num_convert % 16 in tabela_hexa.keys():
            hexadecimal = tabela_hexa[num_convert % 16] + hexadecimal
        else:
            hexadecimal = str(num_convert % 16) + hexadecimal
        
        num_convert = num_convert // 16
    
    print("\n\033[36m< {} convertido para base 16 (hexadecimal), é igual a: {} >\033[m".format(num_save, hexadecimal))
    
else:
    print("\033[31mA opção escolhida não está na lista, tente novamente!\033[m")



""" ==================== Utilizando Funções Para o Cálculo ===================="""

if escolha_converter == 1:
    print("\n\033[36m< {} convertido para base 2 (binário), é igual a: {} >\033[m".format(num_save, bin(num_save)[2:]))
elif escolha_converter == 2:
    print("\n\033[36m< {} convertido para base 8 (octal), é igual a: {} >\033[m".format(num_save, oct(num_save)[2:]))
elif escolha_converter == 3:
    print("\n\033[36m< {} convertido para base 16 (hexadecimal), é igual a: {} >\033[m".format(num_save, hex(num_save)[2:]))
else:
    print("\033[31mA opção escolhida não está na lista, tente novamente!\033[m")
