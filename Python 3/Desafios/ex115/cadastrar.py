def cadastro(base_dados):
    
    nome = input('Nome: ')
    
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            break
    
    dado = f'{nome},{idade}\n'
    
    base = open(base_dados, 'a', encoding='utf-8')
    base.write(dado)
    base.close()
    
    print(f'Novo registro de {nome} adicionado.')
