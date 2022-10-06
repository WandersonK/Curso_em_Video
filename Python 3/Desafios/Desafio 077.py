# Crie uma programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

conjunto_palavras = ('Aviao', 'Elefante', 'Bola', 'Bebe', 'Peixe', 'Futebol', 'Beliscao', 'Papel', 'Basquete', 'Controle',
                    'Triste', 'Gato', 'Golfe', 'Tesoura', 'Colher', 'Pular', 'Galinha', 'Sapo', 'Espirro', 'Martelo')

vogais = 'aeiou'

for palavra in conjunto_palavras:
    contem = ''
    print(f"Na palavra {palavra.upper()} temos", end=" ")
    
    for letra in palavra:
        if letra.lower() in vogais:
            contem += letra.lower() + ' '
    
    print(contem)


#  Forma do Guanabara

for p in conjunto_palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
