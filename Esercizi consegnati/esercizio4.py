'''Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). 
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).'''


print("Calcolo la media dei numeri positivi interi che inserisci")
quanti:int = 0
somma:int = 0
media:int = 0
numeri:list =[]        # lista vuota che conterrà tutti i valori inseriti
x:int = 1           # inizializzo 'x' ad un qualsiasi valore positivo
while True:    # fintanto che il numero inserito è maggiore di 0...
    x = float(input("Dammi un numero, termina inserendo un numero negativo"))
    if x<0:
        break
    else:            # ... nel caso in cui sia positivo ...
        numeri.append(x)       # ... inserisci il numero dentro alla lista
        if x.is_integer():     # se è un intero...
            somma+=x
            quanti+=1
            media=somma/quanti       # ... aggiorna tutte le variabili e calcola la media
print(f"La media dei soli numeri interi inseriti è {media}\nIl numero più grande è {max(numeri)}, il più piccolo è {min(numeri)}")      # stampa la media e il massimo e minimo della lista di numeri