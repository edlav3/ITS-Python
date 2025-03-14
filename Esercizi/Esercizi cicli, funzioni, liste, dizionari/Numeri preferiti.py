'''modifica il programma dell'esercizio 6-2 in modo che ogni persona possa avere più di un numero preferito.
Quindi stampa il nome di ogni persona insieme ai suoi numeri preferiti.'''

preferiti={"Dario": [20, 21], "Marco": [220, 221], "Pino": [200, 201], "Silvio": [202, 203], "Consuelo": [2020, 2021]}
for nome, num in preferiti.items():
    print(f"I numeri preferiti di {nome} sono {num[0]} e {num[1]}")