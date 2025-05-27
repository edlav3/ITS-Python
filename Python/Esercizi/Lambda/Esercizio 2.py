'''
Crea una funzione lambda che accetti due numeri e restituisca la loro somma.
'''

from typing import Callable

a=int(input("Primo numero: "))
b=int(input("Secondo numero: "))

somma:Callable[[int,int], int]=lambda a, b: a+b
print(somma(a, b))