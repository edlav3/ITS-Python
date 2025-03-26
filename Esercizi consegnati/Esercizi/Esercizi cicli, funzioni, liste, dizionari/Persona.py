'''usa un dizionario per memorizzare informazioni su una persona che conosci.
Memorizza il suo nome, cognome, età e città in cui vive. Dovresti avere chiavi come nome, cognome, età e città.
Stampa ogni informazione memorizzata nel tuo dizionario.'''


persona={"nome": "Mario", "cognome":"Rossi", "età":19, "città": "Milano"}

# chiavi=list[persona.keys()]
# valori=list[persona.values()]
# print(chiavi)
# print(valori)
'''metodo alternativo'''

for key, value in persona.items():
    print(f"{key}, {value}")
