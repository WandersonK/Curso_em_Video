# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle, sample

i = 1
alunos = []

alunos.append(input("Nome do 1º aluno: "))
alunos.append(input("Nome do 2º aluno: "))
alunos.append(input("Nome do 3º aluno: "))
alunos.append(input("Nome do 4º aluno: "))

shuffle(alunos)

print("Ordem de apresentação:")

for nome in alunos:
    print(f"O aluno {nome} é o {i}º.")
    i += 1
    
# for i in sample(range(1, 5), 4):
#     print(f"O aluno {alunos[i-1]} é o {i}º.")



