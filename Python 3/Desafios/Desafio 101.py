"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições."""


def voto(ano_nasc):
    from datetime import datetime
    
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



# Forma do Guanabara
def voto_g(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÂO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto_g(nasc))