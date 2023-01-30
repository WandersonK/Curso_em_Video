"""Crie um código em Python que testa se o site Pudim está acessível pelo computador usado."""

import urllib
import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br/')

except:
    print('\033[31mO site Pudim não está acessivel no momento.\033[m')

else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')



# Forma do Guanabara
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessivel no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
    print(site.read())
