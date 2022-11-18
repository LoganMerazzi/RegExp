# Meta caracteres: ^ $ ( )
# *   0 ou n caracteres
# +   1 ou n caracteres
# ?   0 ou 1
# {n} 
# {min,max}
# {1} apenas uma
# {1,} pelo menos uma
# {,10} até 10
# {5,10} entre 5 e 10

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'jO+ãO+',texto, flags=re.I))
print(re.findall(r'jO{1,}ãO{1,}',texto, flags=re.I))
print(re.findall(r've{3}m{1,2}',texto, flags=re.I))
#print(re.sub(r'jO+ãO+', 'Felipe',texto, flags=re.I))


texto2 = 'João ama ser amado'
print(re.findall(r'ama[do]{2}',texto2, flags=re.I))
print(re.findall(r'ama[do]{0,2}',texto2, flags=re.I))
print(re.findall(r'ama[do]*',texto2, flags=re.I))

