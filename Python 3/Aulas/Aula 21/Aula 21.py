def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))

print(f'O fatorial de {n} é {fatorial(n)}')

n1 = fatorial(4)
n2 = fatorial(3)
n3 = fatorial()

print(f'O resultado foi {n1}, {n2} e {n3}')



def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
