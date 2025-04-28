'''
Hai una lista di parole parole = ["cane", "gatto", "elefante", "ratto", "orso"]
Estrai solo le parole con più di 4 lettere usando filter() e lambda.
'''

from typing import Callable
import re

parole = ["cane", "gatto", "elefante", "ratto", "orso"]
piudiquattro:Callable[[list[str]], list[str]]=list(filter(lambda x: re.fullmatch(r"[a-zA-Z]{5,}", x), parole))
print(piudiquattro)