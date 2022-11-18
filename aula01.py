import re

# findall search sub
# compile

string = "Este é um teste de expressões regulares teste"

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'abcd' , string))
print(re.sub(r'teste', 'abcd' , string, count = 1))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))