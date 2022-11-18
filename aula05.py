# Meta caracteres: ^ $ ( )
# *   0 ou n caracteres
# +   1 ou n caracteres
# ?   0 ou 1

import re

texto = '''
<p> Frase 1</p> <p> Frase 2</p> <p> Frase 3</p> <p> Frase 4</p> <div></div>
'''
# modo greedy
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>',texto))
# modo lazy
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>',texto))
# modo lazy, mas sem retornar as tags vazias
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>',texto))
