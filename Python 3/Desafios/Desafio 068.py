# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o taotal de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

divisor = "=-" * 15
vencidas = 0

print(divisor)
print('{:^30}'.format("VAMOS JOGAR PAR OU ÍMPAR"))
print(divisor)

while True:
    escolha_computador = randint(0, 10)

    escolha_usuario = int(input("Digite um valor: "))
    while True:
        par_impar = str(input("Par ou Ímpar? [P/I] "))
        if par_impar in 'PpIi':
            break
    
    if (escolha_computador + escolha_usuario) % 2 == 0:
        resultado_jogada = 'PAR'
    else:
        resultado_jogada = 'ÍMPAR'
    
    print("-" * 30)
    print(f"Você jogou {escolha_usuario} e o computador {escolha_computador}. Total de {escolha_computador + escolha_usuario} DEU {resultado_jogada}")
    print('-' * 30)
    
    if resultado_jogada == 'PAR' and par_impar in 'Pp' or resultado_jogada == 'ÍMPAR' and par_impar in 'Ii':
        print("Você VENCEU!\nVamos jogar novamente...")
        print(divisor)
    else:
        print("Você PERDEU!")
        print(divisor)
        break
    
    vencidas += 1

print(f"GAME OVER! Você venceu {vencidas} vezes.")
