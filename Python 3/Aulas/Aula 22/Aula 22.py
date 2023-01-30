def fatorial(n):
    fa = 1
    for c in range(1, n+1):
        fa *= c
    return fa


num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}")
