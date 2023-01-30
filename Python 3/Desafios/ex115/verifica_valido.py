def verificar(opcao):
    try:
        if int(opcao) not in [1, 2, 3]:
            print('\033[31mERRO! Digite um opção válida!\033[m')
    except:
        print('\033[31mERRO! Digite um opção válida!\033[m')
    else:
        return int(opcao)
    