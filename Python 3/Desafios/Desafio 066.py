# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).

quantidade = somatorio = 0

while True:
    valor = int(input("Digite um valor (999 para parar): "))
    
    if valor == 999:
        break
    
    quantidade += 1
    somatorio += valor

print(f'A soma dos {quantidade} valores foi {somatorio}!')
