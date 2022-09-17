# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input("Informe o primeiro termo da PA: "))

razao = int(input("Informe a razão da PA: "))
print("\nA PA para os dados informados é: ")

continuacao = 10

while continuacao != 0:
    i = 0
    
    while i < continuacao:
        print(primeiro_termo, end=" -> ")
        primeiro_termo += razao
        i += 1
    
    print('PAUSA')
    
    continuacao = int(input("\nDigite 0 Para sair ou um número para continuar a PA: "))
    
print("FIM")



"""   FORMA GUANABARA   """
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
