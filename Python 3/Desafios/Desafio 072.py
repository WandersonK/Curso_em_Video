""" Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

#  Forma inicial
"""
num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    posicao = int(input("Entre 0 e 20, qual número você deseja por extenso? "))
    if posicao in range(0, 21):
        break
    print('Tente novamente. ', end='')

print(f'O número {posicao} por extenso é: {num_extenso[posicao]}')
"""

#  Forma aperfeiçoada
num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    posicao = int(input("Entre 0 e 20, qual número você deseja por extenso? "))
    
    if posicao in range(0, 21):
        print(f'O número {posicao} por extenso é: {num_extenso[posicao]}')
        
        continuar = input('Deseja continuar: [S/N] ')[0]
        
        if continuar in 'Nn':
            break



#  Forma do Guanabara
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[núm]}')
