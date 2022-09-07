""" Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no fianl, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""
from time import sleep

print("\033[35m{0} BEM VINDO AO SISTEMA ESCOLAR WK {0}\033[m".format('='*10))
print("Vamos começar com as notas do aluno para verificação:")

nota1 = int(input("\033[36m1º Nota:\033[m "))
nota2 = int(input("\033[36m2º Nota:\033[m "))

print("\n\033[35mCalculando...\033[m")
sleep(1)
print("\033[35mVerificando...\033[m\n")
sleep(1)

media_aluno = (nota1 + nota2) / 2

if media_aluno >= 7:
    print("\033[32mAPROVADO!\033[m")
    print("PARABÉNS!!! Você foi aprovado com média igual a {:.1f}!".format(media_aluno))
    
elif media_aluno < 5:
    print("\033[31mREPROVADO!\033[m")
    print("Infelizmente você foi reprovado, sua média é igual a {:.1f}!".format(media_aluno))
    
elif media_aluno >= 5 and media_aluno < 7:
    print("\033[33mRECUPERAÇÃO!\033[m")
    print("Você ainda pode ser aprovado, sua média é {:.1f}!".format(media_aluno))
