'''
Che cos'è un file json?
Corrispondono a dei dizionari
'''

import json


modeLettura: str = "r"
encoding: str = "utf-8"
PATH: str = "Python/Appunti/Flask/FileJson.json" # percorso relativo del mio file json (mai usare path assoluto)

with open(PATH, mode=modeLettura, encoding=encoding) as file:
    config: dict = json.load(file) # la funzione load mi permette di caricare il file json nella mia memoria ram
                                   # config diventa un dizionario a tutti gli effetti, contenente i dati del file json
    
    print(config)