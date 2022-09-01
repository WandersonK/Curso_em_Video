# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input("Informe o nome de uma cidade: ").strip()

if cidade.upper().find('SANTO') == 0:
    print(f"{cidade} inicia com SANTO")
else:
    print(f"{cidade} não inicia com SANTO")
    
    
# Forma q o Guanabara fez:
print(cidade[:5].upper() == 'SANTO')