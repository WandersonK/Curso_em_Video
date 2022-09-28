""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
"""

times = ('Palmeiras','Internacional','Fluminense','Flamengo','Corinthians','Athletico-PR','Atlético-MG','América-MG',
         'Goiás','Botafogo','Santos','Bragantino','São Paulo','Fortaleza','Ceará','Coritiba','Avaí','Cuiabá','Atlético-GO','Juventude')

separador = '-=' * 30

print(f"{separador}\nLista de times do Brasileirão: {times}")
print(f'{separador}\nOs 5 primeiros colocados da tabela são: {times[:5]}')
print(f'{separador}\nOs 4 últimos colocados da tabela são: {times[-4:]}')
print(f'{separador}\nTimes em ordem alfabética: {sorted(times)}')

if 'Chapecoense' in times:
    print(f"{separador}\nO time da Chapecoense está na {times.index('Chapecoense') + 1}º posição")
else:
    print(f"{separador}\nA Chapecoense não está na tabela.")
