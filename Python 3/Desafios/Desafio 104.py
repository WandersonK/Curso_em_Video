"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para
aceitar apenas um valor numérico.
Ex:
n = leiaInt('Digite um n')"""

def leiaInt(msg):
    while True:
        digitado = input(msg)
        
        if digitado.isnumeric():
            return digitado
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')



# Forma Guanabara
def leiaInt_g(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

# Programa Principal
n = leiaInt_g('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
