'''un dizionario Python può essere utilizzato per modellare un dizionario reale. Tuttavia, per evitare confusione, chiamiamola glossario.
• Pensa a cinque parole di programmazione che hai imparato nei capitoli precedenti.
Usa queste parole come chiavi nel tuo glossario e memorizza i loro significati come valori.
• Stampa ogni parola e il suo significato come output formattato in modo ordinato.
Potresti stampare la parola seguita da due punti e poi il suo significato, oppure stampare la parola su una riga e poi stampare
il suo significato rientrato su una seconda riga. Usa il carattere di nuova riga (\n) per inserire una riga vuota tra ogni
coppia parola-significato nel tuo output.'''


glossario={"insert":"Inserisce un elemento all'interno di una lista",
           "print": "stampa a schermo un messaggio, valore o variabile",
           "len": "ritorna la lunghezza di un oggetto",
           "lower": "funzione che trasforma tuttii i caratteri di una stringa in minuscolo",
           "remove": "funzione che, in una lista, elimina la prima occorrezza che incontra di un dato valore"}

for funzione, definizione in glossario.items():
    print(f"Funzione: {funzione}\nDefinizione: {definizione}\n\n")