'''Scrivi un programma che esegue le seguenti operazioni:

Il programma prende in input una lista che rappresenta un carrello della spesa. Ogni elemento della lista può essere:

Un prodotto con il formato ("nome", prezzo) (ad esempio, ("mela", 1.5)).
Un prodotto con sconto, rappresentato come ("nome", prezzo, sconto) (ad esempio, ("banana", 2.0, 0.2)).
Un prodotto con una quantità, rappresentato come ("nome", prezzo, quantità) (ad esempio, ("pane", 1.2, 3)).
Il programma deve calcolare il totale del carrello, considerando:

Se un prodotto ha uno sconto, il prezzo sarà ridotto di quel valore.
Se un prodotto ha una quantità, il prezzo verrà moltiplicato per quella quantità.
Ogni prodotto, infine, deve essere aggiunto al totale del carrello.
Al termine, il programma deve stampare il totale del carrello e un messaggio che indica
se il totale è superiore o inferiorea una soglia di spesa (ad esempio, 20.0). Se il totale è superiore alla soglia,
bisogna stampare un messaggio di "spesa alta", altrimenti "spesa bassa".'''


risposta=""
totale=0
soglia=50
carrello={}
risposta=str(input("Vuoi inserire un prodotto? Digita 'si' o 'no: "))
while risposta!="no":
    nomeprodotto=str(input("Nome del prodotto: "))
    prezzo=float(input("Prezzo:  "))
    sconto=str(input("L'articolo è scontato? Digita 'si' o 'no': "))
    if sconto=="si":
        valoresconto=float(input("Di quanto è lo sconto?\nInserisci il valore in decimale, esempio: se lo sconto è del 20%, inserisci 0.2\nSconto:"))
        prezzo=prezzo-(prezzo*valoresconto)
        quanti=int(input(f"Quanti articoli {nomeprodotto} vuoi acquistare: "))
        carrello[nomeprodotto]=quanti
        prezzofinale=prezzo*quanti
        totale+=prezzofinale
    else:
        quanti=int(input(f"Quanti articoli {nomeprodotto} vuoi acquistare: "))
        carrello[nomeprodotto]=quanti
        prezzofinale=prezzo*quanti
        totale+=prezzofinale
    
    risposta=str(input("Vuoi inserire un altro prodotto? Digita 'si' o 'no: "))

nomi=list(carrello.keys())
numeroprodotto=list(carrello.values())
print("\nHai acquistato: ")
for i in range(len(nomi)):
    print(f"{nomi[i]} x{numeroprodotto[i]}", sep=" -- ")



print(f"Per un totale è di {totale:.2f}€")