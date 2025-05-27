'''
Scrivi una funzione check_product_code(code) che verifica se il codice è nel formato PROD-1234-AB.

Esempio:

check_product_code("PROD-9876-ZX")  # True
check_product_code("PROD-99-ZX")    # False
'''

import re

def check_product_code(code:str):
    risultato=bool(re.fullmatch(r"^PROD+-\d{4}-[A-Z]{2}$", code))
    print(risultato)

check_product_code("PROD-9876-ZX")
check_product_code("PROD-99-ZX")