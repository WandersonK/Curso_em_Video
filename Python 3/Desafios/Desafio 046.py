# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print("\033[36m{0} CONTAGEM REGRESSIVA PARA OS FOGOS {0}\033[m".format('*' * 10))

for t in range(10, -1, -1):
    print(f'\033[32m{t}\033[m')
    sleep(1)

print("\n\033[35mAEEEEEEEEE FOGOOOOOOOSSSS!!!\033[m")
