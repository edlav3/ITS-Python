'''
Scrivi una funzione find_codes(text) che trova tutte le parole lunghe 8 caratteri,
con lettere maiuscole e/o numeri.

Esempio:

text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
find_codes(text)  # ['AB12CD34', '12345678', 'XYZZYZZZ']
'''
import re

def find_codes(text:str):
    risultato=re.findall(r"[a-zA-Z0-9]{8}", text)
    print(risultato)

text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
find_codes(text)  # ['AB12CD34', '12345678', 'XYZZYZZZ']