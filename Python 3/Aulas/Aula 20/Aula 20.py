"""
def lin():
    print('-' * 30)


lin()
print('    CUSO EM VÍDEO    ')
lin()
lin()
print('    APRENDA PYTHON    ')
lin()
lin()
print('    GUSTAVO GUANABARA    ')
lin()
"""

"""
def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


# Programa Principal
título('    CURSO EM VÍDEO    ')
título(' PYTHON É MUITO BOM! ')
título('Oi')
"""

# Exemplo de rotina
"""
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)
"""


# Resolvendo a repetição com função
"""
def soma(a, b):
    s = a + b
    print(s)


#   Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
"""


# Mais exemplos
"""
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#   Programa Principal
soma(b=4, a=5)
soma(7, 2)
"""


# Empacotamento
"""
def contador(* núm):
    # print(núm)

    # for valor in núm:
    #     print(valor, end=' ')
    # print('FIM!')

    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
"""


# Dobrando os valores de uma lista
"""
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
"""


# Utilizando ainda empacotamento
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
