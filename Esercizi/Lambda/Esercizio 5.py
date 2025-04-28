'''
Crea una funzione lambda che prenda un numero e ritorni "pari"
se è divisibile per 2, altrimenti "dispari".
'''

from typing import Callable

x=int(input("Dammi un numero: "))
verifica:Callable[[int], str]=lambda x: "Pari" if x%2==0 else "Dispari"
print(verifica(x))