'''Scrivere un programma che permetta all'utente di inserire una serie di parole in input,
terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.'''


parola=""   # definisco una variabile 'parola' contente una stringa vuota
while True:       # fintanto che 'parola' è diversa da 'fine'...
    parola : str = str(input("Inserisci una parola, digita 'fine' per terminare"))     # ... aggiorna 'parola' con la stringa inserita dall'utente
    if parola=="fine":
        break      # interrompi quando l'utente digita 'fine'
    elif parola[0] == parola[len(parola)-1]:        # confronto il primo e l'ultimo carattere
        print("Il primo e ultimo carattere sono uguali\n")
    else:
        print("Il primo e ultimo carattere non sono uguali\n")