'''Esercizio 3C-00A. Scrivere un programma in Python che richieda all'utente di inserire un numero intero rappresentante
il numero di neonati e utilizzi lo statement match per fornire una risposta appropriata:

- Se il numero inserito è 1, stampare "Congratulazioni!"
- Se il numero inserito è 2, stampare "Wow! Gemelli!"
- Se il numero inserito è 3, stampare "Wow! Tre!"
- Se il numero inserito è 4, stampare "Mamma mia Quattro! Wow!"
- Se il numero inserito è 5, stampare "Incredibile! Cinque!"
- Altrimenti, stampare "Non ci credo! n bambini!", sostituendo n con il numero inserito.

Expected Output:

Inserire il numero di neonati: 2
Wow! Gemelli!

- - - - - - - - - - - - - - - - - -

Inserire il numero di neonati: 5
Incredibile! Cinque!

- - - - - - - - - - - - - - - - - -

Inserire il numero di neonati: 7
Non ci credo! 7 bambini!'''


quanti: int = int(input("Inserire il numero di neonati:")) # chiedo all'utente l'input

match quanti: # poniamo sotto esame la variabile 'quanti' fornita dall'utente
    case 1: # se ha inserito un bambino
        print("Congratulazioni!")
    case 2: # se ha inserito due bambini
        print("Wow! Gemelli!")
    case 3: # se ha inserito tre bambini
        print("Wow! Tre!")
    case 4: # se ha inserito quattro bambini
        print("Mamma mia Quattro! Wow!")
    case 5: # se ha inserito cinque bambini
        print("Incredibile! Cinque!")
    case _: # se ha inserito più di 5 bambini
        print(f"Non ci credo! {quanti} bambini!")