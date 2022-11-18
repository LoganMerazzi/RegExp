# Meta caracteres: ^ $ ( )
#[abc]
# [a-z]+
# (abc | def) \1 <-- Quantificador
# (  )  \1
# ( ) ( )  \1 \2
# ( () ) \1 \2 (ordem de referência "de fora para dentro")
# ( () ) () \1 \2 \3
# Ideia: Pensar na ordem dos grupos pela abertura dos parênteses.

import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <p>Frase 4</p> <div>1</div>
'''
# modo lazy, mas sem retornar as tags vazias
# print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>',texto))
# Vai retornar apenas o que foi colocado em memória, ou seja, apenas o conjunto criado
# print(re.findall(r'<([pdiv]{1,3})>.+?<\/\1>',texto))
# Vai dar um problema, devido ao grupo interno, ele está referenciando ao grupo maior
#print(re.findall(r'(<([pdiv]{1,3})>.+?<\/\1>)',texto))
#Funciona, pois estou pedindo para retornar o segundo grupo (o grupo menor)
# pprint(re.findall(r'(<([pdiv]{1,3})>.+?<\/\2>)',texto))


# tags = re.findall(r'(<([pdiv]{1,3})>.+?<\/\2>)',texto)
# pprint(tags)

# for tag in tags:
#     print(tag)
#     um, dois = tag
#     print(um, dois)
    
# tags = re.findall(r'(<([pdiv]{1,3})>(.+?)<\/\2>)',texto)
# pprint(tags)

# for tag in tags:
#     um, dois, tres = tag
#     print(tres)
    
# Para indicar que o grupo seja criado, mas não seja salvo em memória, colocar o '?:' 
# tags = re.findall(r'(<([pdiv]{1,3})>(?:.+?)<\/\2>)',texto)
# print(tags)

# cpf = '654.963.159-00'
# # validar o formato do cpf...
# print(re.findall(r'[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}', cpf))
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
# #                    ~~ Apenas para quantificar, não quero exibir
# # Criando grupos nomeados
# tags = re.findall(r'(<(?P<tag>[pdiv]{1,3})>(?:.+?)<\/(?P=tag)>)',texto)
# print(tags)

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)',r'\1"\3"\4',texto))

