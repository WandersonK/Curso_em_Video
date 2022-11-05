"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
comprimento) e mostre a área do terreno."""


def área(larg, comp):
    print(f'A área de um terreno {larg}x{comp} é de {larg * comp:.1f}m².')


# Programa Principal
print(' Controle de Terrenos')
print('-' * 22)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

área(largura, comprimento)
