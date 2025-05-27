'''
Scrivi una funzione extract_emails(text) che prende un testo e restituisce tutte le email trovate.

Esempio:

text = "Contattaci a info@azienda.com oppure support@help.org"
extract_emails(text)  # ['info@azienda.com', 'support@help.org']
'''

import re

def extract_emails(text:str):
    risultato=re.findall(r"\S+@\S+", text)
    print(risultato)

text = "Contattaci a info@azienda.com oppure support@help.org"
extract_emails(text)