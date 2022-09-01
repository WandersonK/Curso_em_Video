""" Faça um programa que leia uma frase pelo teclado e mostre:
-> Quantas vezes aparece a letra "A".
-> Em que posição ela aparece a primeira vez.
-> Em que posição ela aparece a última vez.
"""

frase = str(input("Digite um frase: ")).strip()

if 'A' in frase.upper():
    print(f"A letra 'A' aparece {frase.upper().count('A')} veze(s).")
    print(f"A primeira letra 'A' está na posição {frase.upper().find('A') + 1}.")
    print(f"A última letra 'A' está na posição {frase.upper().rfind('A') + 1}.")
    
else:
    print("Não existe letra 'A' na frase.")
