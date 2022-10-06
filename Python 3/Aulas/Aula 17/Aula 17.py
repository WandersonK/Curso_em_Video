num = (2, 5, 9, 1)
# num[2] = 3  # Não aceita pois a tupla é imutável
print(num)

num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7 # Não aceita pois o indice 4 não existe
num.append(7) # Forma correta de inserir um novo valor
num.sort() # Ordenação crescente
print(num)
num.sort(reverse=True) # Ordenação decrescente
print(num)
num.insert(2, 2) # Insere na posição 2 o número 2
if 4 in num:
    num.remove(4) # Vai remover o número 4 caso ele exista na lista
print(num)
num.remove(2) # Ele remove a primeira ocorrência, ou seja, o primeiro 2
print(num)
print(f'Esta lista tem {len(num)} elementos.')
# num.pop(2)


#####
valores = list()

valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


#####
valores = list()

for cont in range(0, 5):
    valores.append(cont)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


#####
a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')

b[2] = 8 # A lista "a" e "b" estão ligadas, então alterando a lista "b", a lista "a" também terá alteração
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Para copiar uma lista, pode-se fazer da seguinte maneira
a = [2, 3, 4, 7]
b = a[:]
# b = a.copy()
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
