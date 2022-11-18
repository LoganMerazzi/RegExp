# ( ... ) \1
# ( ... ) ( ... )   \1   \2
# ( () )  \1   \2
# ( () ) ( ... )   \1   \2   \3
 
import re

valor = 'Legal!! <img class="react-emoji" src="./assets/upload/react/a2f5313b2aa67d5bbe860a849f3308f0.png" title=":bolo:" alt=":bolo:"/> demais <img class="react-emoji" src="./assets/upload/react/a2f5313b2aa67d5bbe860a849f3308f1.png" title=":cake:" alt=":cake:"/> isso aqui  <img class="react-emoji" src="./assets/upload/react/a2f5313b2aa67d5bbe860a849f3308f1.png" title=":[:" alt=":[:"/>'

# Pega o arquivo
print(re.findall(r'([a-z0-9]+.png)',valor))
# Pega a tag inteira
print(re.findall(r'(<img.*?([a-z0-9]+.png).*?/>)',valor))

imgs = re.findall(r'(<img.*?([a-z0-9]+.png).*?/>)',valor)

valor2 = valor
for img in imgs:
    print(img)
    um, dois = img
    valor2 = re.sub(um,'UTFXXX',valor2)
    dois = re.search(r'[0-9a-z]+',dois)
print(valor)
print(valor2)
print(dois)


# ideia:
