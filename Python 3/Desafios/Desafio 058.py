# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint 

palpites = 1
num_computador = randint(0, 10)

print("BEM VINDO AO JOGO!")

num_escolhido = int(input("Adivinhe o número que eu estou pensando (0 a 10): "))

while num_escolhido != num_computador:
    print("\033[31mQue pena, você errou!\033[m tente novamente!")
    num_escolhido = int(input("\033[35m>>\033[m "))
    palpites += 1

print("\033[35mMassa demais, você acertou com {} palpites!\033[m".format(palpites))
