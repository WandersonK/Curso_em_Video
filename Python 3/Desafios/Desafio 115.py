"""Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""

from ex115.cadastrar import cadastro
from ex115.consultar import consulta
from ex115.menu import menu
from ex115.verifica_valido import verificar

base_dados = 'C:/Users/wan01/Documents/Curso_em_Video/Python 3/Desafios/ex115/base_dados.txt'


while True:
    menu()
    opcao = verificar(input('\033[33mSua Opção: \033[m'))
    
    if opcao in [1, 2, 3]:
        if opcao == 1:
            consulta(base_dados)
        if opcao == 2:
            cadastro(base_dados)
        if opcao == 3:
            print('== Até Logo! ==')
            break
    