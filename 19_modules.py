import sys
print(sys.path)

import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+',text)
print(result)

import time
onix = time.time()

horaNormal = time.asctime(time.localtime())
print(horaNormal)

import collections

t1 = 'Hola mucho gusto como estan pues'
resultado = collections.Counter(t1)
print(resultado)