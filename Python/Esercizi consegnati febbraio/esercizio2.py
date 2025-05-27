'''Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa.
Il risultato deve essere visualizzato in output.'''


spazi=0      # inizializzo a 0 una variabile 'spazi'
stringa:str = str(input("Posso contare gli spazi che inserisci, prova a digitare qualcosa!"))   # chiedo all'utente una stringa
for i in range(len(stringa)-1):
    if stringa[i] == " ":
        spazi += 1       # mentre scorro la lista, aumento di 1 la variabile 'spazi 'ad ogni carattere " " incontrato
print(f"Hai inserito {spazi} spazi")