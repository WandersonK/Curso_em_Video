def consulta(base_dados):

    print(f"{'-' * 50}\n{'PESSOAS CADASTRADAS':^50}\n{'-' * 50}")
    base = open(base_dados)
    
    for dado in base.readlines():
        print(f"{dado.split(',')[0]:<40}{dado.split(',')[-1].split()[0]} anos")

    base.close()
