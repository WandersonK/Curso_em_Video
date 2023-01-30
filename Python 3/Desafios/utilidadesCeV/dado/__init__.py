def leiaDinheiro(entrada):
    while True:
        valor = input(entrada).strip().replace(',', '.', 1)
        if valor.replace('.', '', 1).isnumeric():
            return float(valor)
        else:
            print(f'\033[31mERRO: "{valor}" é um preço inválido!\033[m')


# Forma do Guanabara
"""
def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)
"""
