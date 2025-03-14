'''inizia con il programma che hai scritto per l'esercizio 6-1.
Crea due nuovi dizionari che rappresentano persone diverse e memorizza tutti e tre i dizionari in un elenco chiamato persone.
Esegui un ciclo nell'elenco di persone. Mentre esegui un ciclo nell'elenco, stampa tutto ciò che sai su ciascuna persona.'''


persona1={"nome": "Mario", "cognome":"Rossi", "età":19, "città": "Milano"}
persona2={"nome": "Mirko", "cognome":"Carota", "età":26, "città": "Roma"}
persona3={"nome": "Matteo", "cognome":"Lasagna", "età":22, "città": "Bologna"}

persone=[persona1, persona2, persona3]

for i in persone:
    print(f"Nome: {i['nome']}, Cognome: {i['cognome']}, anni: {i['età']}, città: {i['città']}\n")

# oppure:
# for i in range(len(persone)):
#   print(persone[i])