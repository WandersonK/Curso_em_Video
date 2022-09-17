# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).

contador = condicao = somatorio = 0

while condicao != 999:
    
    condicao = int(input("Informe um número inteiro ou 999 para sair: "))
    
    if condicao != 999:
        contador += 1
        somatorio += condicao

print("Foram digitados {} números, a soma entre eles é {}".format(contador, somatorio))



"""   FORMA GUANABARA   """
núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
