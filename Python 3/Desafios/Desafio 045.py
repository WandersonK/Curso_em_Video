# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

print("\033[34m{0} JOGANDO JOKENPÔ {0}\033[m".format('=' * 10))

print("Escolha entre: \033[36mPedra\033[m, \033[36mPapel\033[m ou \033[36mTesoura\033[m.")
escolha_user = str(input("\033[33m>> \033[m")).strip().title()

escolha_computer = choice(['Pedra', 'Papel', 'Tesoura'])

print("JO")
sleep(0.7)
print("KEN")
sleep(0.7)
print("PO!!!\n")


def print_escolhas(escolha_computer, escolha_user, alternativa):
    print("O computador escolheu \033[31m{}\033[m e você escolheu \033[31m{}\033[m.".format(escolha_computer, escolha_user))

    if escolha_computer == alternativa:
        print("\033[32mGenial!!! Você ganhou.\033[m")
    else:
        print("\033[33mQue pena, você perdeu. O computador venceu!\033[m")


if escolha_user == escolha_computer:
    print("O computador escolheu \033[31m{}\033[m e você escolheu \033[31m{}\033[m.".format(escolha_computer, escolha_user))
    print("\033[35mO jogo empatou!\033[m")
        
elif escolha_user == 'Tesoura':
    print_escolhas(escolha_computer, escolha_user, 'Papel')
        
elif escolha_user == 'Papel':
    print_escolhas(escolha_computer, escolha_user, 'Pedra')
        
elif escolha_user == 'Pedra':
    print_escolhas(escolha_computer, escolha_user, 'Tesoura')
        
else:
    print("\033[31mA opção inserida é inválida, tente novamente.\033[m")
