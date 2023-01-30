"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""

def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        
        except KeyboardInterrupt:
            print('\033[31m\nUsuário preferiu não digitar esse número.\033[m')
            return 0
        
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        
        else:
            return valor


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        
        except KeyboardInterrupt:
            print('\033[31m\nUsuário preferiu não digitar esse número.\033[m')
            return 0
        
        except:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        
        else:
            return valor


inteiro = leiaInt('Digite um Inteiro: ')
real = leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')



# Forma do Guanabara
def leiaInt_g(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31m\nUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat_g(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31m\nUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt_g('Digite um Inteiro: ')
n2 = leiaFloat_g('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
