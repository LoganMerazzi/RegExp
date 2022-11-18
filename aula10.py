import re


cpf = '858.951.789-00'
cpf_regexp = re.compile(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$')

# print(cpf_regexp.search('cpf'))

# Modo 1

# ip_regexp = re.compile(r'''
#     ^
#     (?:
#     25[0-5] |
#     2[0-4][0-9] |
#     1[0-9]{2} |
#     [1-9][0-9] |
#     [0-9] 
#     )
#     \.
#     (?:
#     25[0-5] |
#     2[0-4][0-9] |
#     1[0-9]{2} |
#     [1-9][0-9] |
#     [0-9] 
#     )
#     \.
#     (?:
#     25[0-5] |
#     2[0-4][0-9] |
#     1[0-9]{2} |
#     [1-9][0-9] |
#     [0-9] 
#     )
#     \.
#     (?:
#     25[0-5] |
#     2[0-4][0-9] |
#     1[0-9]{2} |
#     [1-9][0-9] |
#     [0-9] 
#     )
#     $
# ''', flags=re.X) # Poderia ser re.VERBOSE, para permitir comentar na expressão


# Modo 2
# ip_regexp = re.compile(r'''
#     ^    
#     (?:
#         (?:
#         25[0-5] |
#         2[0-4][0-9] |
#         1[0-9]{2} |
#         [1-9][0-9] |
#         [0-9] 
#         )
#         \.
#     ){3}
#     (?:
#         25[0-5] |
#         2[0-4][0-9] |
#         1[0-9]{2} |
#         [1-9][0-9] |
#         [0-9] 
#     )
#     $
# ''', flags=re.X) # Poderia ser re.VERBOSE, para permitir comentar na expressão


## Modo 3
#ip_regexp = re.compile(r'''
#    ^    
#    (?:
#        (?:
#        25[0-5] |
#        2[0-4][0-9] |
#        1[0-9]{2} |
#        [1-9][0-9] |
#        [0-9] 
#        )
#        \.? # Isso faz com que o IP 0.0.0.0. seja válido, para contornar, deve-se usar a borda logo abaixo
#    ){4}
#    \b
#    $
#''', flags=re.X) # Poderia ser re.VERBOSE, para permitir comentar na expressão
#
# Modo 3, em uma linha

ip_regexp = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$')

for i in range(301):
  ip = f'{i}.{i}.{i}.{i}'
  print(ip, ip_regexp.findall(ip))