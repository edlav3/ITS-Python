'''
Scrivi una funzione find_dates(text) che trova tutte le date in formato italiano (dd/mm/yyyy) in un testo.

Esempio:

text = "Le date importanti sono 09/04/2025 e 15/08/2023."
find_dates(text)  # ['09/04/2025', '15/08/2023']
'''

import re

def find_dates(text:str):
    risultato=re.findall(r"\d{2}/\d{2}/\d{4}", text)
    print(risultato)


text = "Le date importanti sono 09/04/2025 e 15/08/2023."
find_dates(text)  # ['09/04/2025', '15/08/2023']