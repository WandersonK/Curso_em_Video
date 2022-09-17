# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = 'S'
media = 0
lista_digitados = []

while continuar == 'S':
    num_digitado = int(input("Informe um número inteiro: "))
    
    lista_digitados.append(num_digitado)
    
    media += num_digitado
    continuar = str(input("Deseja continuar? [S/N] ")).upper()
    
lista_digitados.sort()

print()
print(f"Os números digitados foram: {lista_digitados}")
print(f"A média entre ele é igual a {media / len(lista_digitados)}")
print(f"O menor valor é o {lista_digitados[0]}")
print(f"O maior valor é o {lista_digitados[-1]}")




"""   FORMA GUANABARA   """
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            meior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'. format(maior, menor))
