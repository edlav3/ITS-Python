'''
Scrivi una funzione is_integer(s) che restituisce True se la stringa è un numero intero (positivo o negativo), False altrimenti.

Esempio:

is_integer("123")      # True
is_integer("-456")     # True
is_integer("12.3")     # False
'''
import re

def is_integer(stringa:str) -> bool:
    risultato=bool(re.fullmatch(r"-?\d+", stringa))
    return risultato

print(is_integer("123"))
print(is_integer("-456"))
print(is_integer("12.3"))