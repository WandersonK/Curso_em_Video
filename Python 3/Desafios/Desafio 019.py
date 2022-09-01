# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import randint, choice

aluno1 = input("Nome do aluno 1: ")
aluno2 = input("Nome do aluno 2: ")
aluno3 = input("Nome do aluno 3: ")
aluno4 = input("Nome do aluno 4: ")

# num_random = randint(1, 4)
#
# if num_random == 1:
#     print(f"O aluno {aluno1} apagará o quadro.")
# elif num_random == 2:
#     print(f"O aluno {aluno2} apagará o quadro.")
# elif num_random == 3:
#     print(f"O aluno {aluno3} apagará o quadro.")
# else:
#     print(f"O aluno {aluno4} apagará o quadro.")

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

print('O aluno escolhido foi {}'.format(choice(lista_alunos)))