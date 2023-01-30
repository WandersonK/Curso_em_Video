"""Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""

from ex115.cadastrar import cadastro
from ex115.consultar import consulta
from ex115.menu import menu
from ex115.verifica_valido import verificar

# base_dados = 'C:/Users/wan01/Documents/Curso_em_Video/Python 3/Desafios/ex115/base_dados.txt'
base_dados = '/home/wanderson/Documentos/Curso_em_Video/Python 3/Desafios/ex115/base_dados.txt'


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



# Forma do Guanabara

from ex115.forma_guanabara.lib.interface import *
from ex115.forma_guanabara.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu_g(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
    