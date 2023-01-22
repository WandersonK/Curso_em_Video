"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função."""

def notas(*lista_notas, sit=False):
    
    """
    -> Função para analisar notas e situações de váris alunos.
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
print(resp)
