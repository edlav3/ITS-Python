percorso: str= "Appunti/CartellaAppuntiFile/esempio2.txt"
modalita: str= "r"
encoding: str= "utf-8"

file=open(percorso)

output: str=file.read()
print(output) # viene stampato il numero di caratteri del file

'''
Vediamo un modo alternativo per scrivere la stessa cosa ma con meno codice
'''

with open("Appunti/CartellaAppuntiFile/esempio2.txt", "r") as file:
    print(file.read())

'''
Questa scrittura si chiama context manager, definisco un contesto valido solo all'internodi questa struttura
Un context manager è una 'classe' e quando si entra nel blocco di codice with, viene richiamato quello dentro la funzione open,
dopo la funzione open, viene eseguito il file ma implicitamente succede il file.close, poi viene eseguito il print, e il file viene chiuso in automatico 
'''

with open("Appunti/CartellaAppuntiFile/esempio2.txt", "r") as mario:
    print(mario.read())  # non è necessario che il file si chiami con lo stesso nome con cui l'abbiamo dichiarato

