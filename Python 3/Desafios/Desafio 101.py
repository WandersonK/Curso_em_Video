"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições."""


from datetime import datetime

def voto(ano_nasc):
    
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasc
    
    if 70 > idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'



print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))

print(voto(nasc))
