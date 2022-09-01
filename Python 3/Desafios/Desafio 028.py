""" Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint 
from time import sleep

num_computador = randint(0, 5)

print("BEM VINDO AO JOGO!")

num_escolhido = int(input("Adivinhe o número que eu estou pensando (0 a 5): "))

print("Hmmmm...")

sleep(1)

if num_escolhido == num_computador:
    print("\033[35mMassa demais, você acertou!\033[m")
else:
    print("\033[31mQue pena, você errou!\033[m O número pensado foi\033[31m", num_computador)
    
