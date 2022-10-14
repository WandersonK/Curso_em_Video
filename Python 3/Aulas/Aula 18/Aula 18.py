teste = list()
teste.append('Wanderson')
teste.append(25)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)


galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

print(galera[0])
print(galera[0][0])
print(galera[2][1])

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')


galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[0] >= 21:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
