# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado foi negativo.

while True:
    
    valor_tabuada = int(input("Quer ver a tabuada de qual valor? "))
    print('-' * 30)
    
    if valor_tabuada < 0:
        break
    
    for i in range(1, 11):
        print(f'{valor_tabuada} x {i} = {valor_tabuada * i}')
    
    print('-' * 30)

print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
