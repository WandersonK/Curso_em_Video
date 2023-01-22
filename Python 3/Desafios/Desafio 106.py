"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavara 'FIM', o programa se encerrará.
OBS: use cores."""

from time import sleep


def help_comando(comando_digitado):
    print("\033[7m", end="")
    help(comando_digitado)
    print("\033[m", end="")

    sleep(1)


while True:

    print("\033[42m", end="")
    print(f"{'~' * 27}\n  SISTEMA DE AJUDA PyHELP\n{'~' * 27}")
    print("\033[m", end="")
    sleep(0.5)
    comando = input('Função ou Biblioteca > ')
    texto_apresentação = f"Acessando o manual do comando '{comando}'"

    if comando.lower() == 'fim':
        print("\033[41m", end="")
        print(f"{'~' * 13}\n  ATÉ LOGO!\n{'~' * 13}")
        print("\033[m", end="")

        break

    print("\033[44m", end="")
    print(f"{'~' * (len(texto_apresentação) + 4)}\n  {texto_apresentação}\n{'~' * (len(texto_apresentação) + 4)}")
    print("\033[m", end="")

    sleep(1)

    help_comando(comando)



# Forma do Guanabara
c = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7m'        # 6 - branco
    )


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

título('ATÉ LOGO!', 1)
