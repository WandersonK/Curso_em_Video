""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Sele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

print("Informe seu sexo:")

sexo = int(input(
"""> \033[31m1\033[m - Masculino
> \033[31m2\033[m - Feminino
\033[31m>>\033[m """
))

if sexo == 1:

    ano_nascimento = int(input("Em que ano você nasceu? "))
    ano_hoje = date.today().year

    if ano_hoje - ano_nascimento < 18:
        anos_restantes = 18 - (ano_hoje - ano_nascimento)
        print("\033[32mVocê ainda irá se alistar no serviço militar.\033[m")
        print(f"Falta(m) \033[32m{anos_restantes} ano(s)\033[m para você se alistar.")
        print(f"Seu alistamento será em {ano_hoje + anos_restantes}.")

    elif ano_hoje - ano_nascimento == 18:
        print("\033[35mHora de se alistar, você já tem 18 anos.\033[m")
        print("Fique atento ao prazo.")
        
    else:
        anos_passados = (ano_hoje - ano_nascimento) - 18
        print("\033[31mO prazo para seu alistamento já passou!\033[m")
        print("Se passaram \033[31m{} ano(s)\033[m do seu prazo.".format(anos_passados))
        print("Você devia ter se alistado em {}.".format(ano_hoje - anos_passados))

elif sexo == 2:
    print("Você não precisa realizar o alistamento.")
    
else:
    print("Opção Inválida, tente novamente!")
