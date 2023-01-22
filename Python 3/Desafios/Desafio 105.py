"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função."""

def notas(*lista_notas, sit=False):
    
    """
    -> Função para analisar notas e situações de vários alunos.
    :param lista_notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicado se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    
    dic_infos = dict()
    
    dic_infos['total'] = len(lista_notas)
    dic_infos['maior'] = max(lista_notas)
    dic_infos['menor'] = min(lista_notas)
    dic_infos['média'] = sum(lista_notas) / len(lista_notas)
    
    if sit:
        if dic_infos['média'] < 5:
            dic_infos['situação'] = 'RUIM'
        elif dic_infos['média'] >= 7:
            dic_infos['situação'] = 'BOA'
        else:
            dic_infos['situação'] = 'RAZOÁVEL'
    
    return dic_infos


print('-'*30)

resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
# print(resp)
help(notas)



# Forma do Guanabara
def notas_g(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicado se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Programa Principal
resp = notas_g(5.5, 2.5, 1.5, sit=True)
# print(resp)
help(notas_g)
