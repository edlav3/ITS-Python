'''
Hai la seguente lista numeri = [5, 12, 17, 18, 24, 32]. Usa filter()
con una lambda per ottenere solo i numeri pari.
'''

from typing import Callable

numeri = [5, 12, 17, 18, 24, 32]
lista_pari:list[int]=list(filter(lambda x:x%2==0, numeri))
print(lista_pari)