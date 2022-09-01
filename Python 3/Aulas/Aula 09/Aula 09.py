frase = 'Curso em Vídeo Python'
frase_espaco = '   Aprenda Python  '

# Fatiamento
print("## Fatiamento ##")
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:14])
print(frase[15:])
print(frase[9::3])
print()

# Análise
print("## Análise ##")
print(len(frase))
print(frase.count('o'))
print(frase.upper().count('O'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Cursos' in frase)
print()

# Transformação
print("## Transformação ##")
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

print(frase_espaco.strip())
print(frase_espaco.rstrip())
print(frase_espaco.lstrip())
print()

# Divisão
print("## Divisão ##")
print(frase.split())
print()

# Junção
print("## Junção ##")
print('-'.join(frase.split()))
