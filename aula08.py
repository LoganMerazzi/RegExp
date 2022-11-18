# \w --> [a-zA-Z0-9À-ú_]
# \w --> [a-zA-Z0-9_] -> re.A / re.ASCII
# \W --> negação do grupo acima ([^a-zA-Z0-9À-ú_])
# \d --> [0-9] digitos
# \D --> [^0-9] Desconsidera os digitos
# \s --> Qualquer tipo de espaço [ \r\n\f\t]
# \s --> Qualquer tipo de espaço [^ \r\n\f\t]
# \b --> "borda": String vazia no começo ou fim da palavra
# \b --> "não borda": String vazia no começo ou fim da palavra

# Flags:
# re.A -> ASCII 
# re.I -> IGNORECASE
# RE.m -> MULTILINE ^ $ 
# RE.S -> DOTALL
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

# print(re.findall(r'[a-z]+',texto,flags=re.I))
# print(re.findall(r'[A-Za-z]+',texto))
# print(re.findall(r'[A-Za-z0-9]+',texto))
#print(re.findall(r'[A-Za-z0-9À-ú]+',texto))
#                             ~~~ -> Abrange todos os acentos (em teoria)
#print(re.findall(r'\w+',texto))
#                  ~~ -> Shorthand para todas as letras
# Vai se comportar como no javascript, desconsiderando os acentos
#print(re.findall(r'\w+',texto, flags=re.ASCII)) # poderia ser re.A nas flags

#print(re.findall(r'\W+',texto, re.ASCII))

# print(re.findall(r'\d+',texto))
# print(re.findall(r'\D+',texto))

# print(re.findall(r'\s+',texto))
#print(re.findall(r'\S+',texto))

# print(re.findall(r'\bflo\w+',texto, re.I))
# print(re.findall(r'\be\w+',texto, re.I))
# print(re.findall(r'\w+e\b',texto, re.I))
# print(re.findall(r'\b\w{4}\b',texto, re.I))
# print(re.findall(r'\w{4}',texto, re.I))
# print(re.findall(r'flo\B',texto, re.I))


# texto = '''
# 123.366.456-87 ASD
# 678.364.354-85 BGT
# 567.765.123-65
# '''

# print(re.findall(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', texto, re.MULTILINE))

texto2 = '''O João gosta de folia 
E adora ser amado'''

print(re.findall(r'^o.*o$', texto2, re.I | re.S))