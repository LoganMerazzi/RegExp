# Meta caracteres: 
# ^ Começa com
# $ Termina
# [^a-z] --> Qualquer coisa que não esteja entre a e z

import re
from pprint import pprint

cpf = 'a 654.963.159-00 a' # --> Vai trazer uma lista vazia por causa do ^ e do $
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))

cpf = '654.963.159-00'
print(re.findall(r'[^a-z]+', cpf))
print(re.findall(r'[^0-9]+', cpf))

