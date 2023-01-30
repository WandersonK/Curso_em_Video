# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro:
#     # print(f'Infelizmente tivemos um problema :(')
#     print(f'Problema encontrado foi {erro.__class__}')
#     print(f'Problema encontrado foi {erro.__cause__}')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte sempre! Muito Obrigado!')


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')
