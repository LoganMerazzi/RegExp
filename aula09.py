import re
from pprint import pprint
# "Lookbehind"
# Quero encontrar a palavra Merazzi, mas apenas se tiver a palavra Logan Antes
# lookahead: o contrário.

texto = '''
ONLINE 192.168.0.100 GLHK active
OFFLINE 192.168.0.101 GLHK inactive
OFFLINE 192.168.0.102 GLHK active
ONLINE 192.168.0.103 GLHK active
ONLINE 192.168.0.104 GLHK inactive
OFFLINE 192.168.0.105 GLHK active
'''

# # positive lookahead assertion
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)',texto))
# # Negative lookahead assertion
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)',texto))
# pprint(re.findall(r'(?=.*[^in]active).+',texto))

# positive lookbehind assertion
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+',texto))
# negative lookbehind assertion
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+',texto))

