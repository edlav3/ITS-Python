'''
Scrivi una funzione moltiplicatore(n)
che ritorni una lambda che moltiplica un valore per n.

Esempio d'uso:

per_due = moltiplicatore(2)
print(per_due(10))  # Output: 20
'''

from typing import Callable

n=int(input("Inserisci un numero che vuoi moltiplicare per tre: "))
per_tre:Callable[[int], int]=lambda x:x*3
print(per_tre(n))