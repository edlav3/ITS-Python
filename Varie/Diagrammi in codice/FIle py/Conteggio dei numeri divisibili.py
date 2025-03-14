'''Progettare un algoritmo che richieda all’utente di inserire un valore intero positivo n.
Se n è negativo, il programma termina mostrando un messaggio di errore. Se n è positivo:

l’utente può inserire 10 numeri interi;
contare quanti di questi numeri sono divisibili per n.
Mostrare in output il risultato del conteggio.'''

num=int(input("Dammi un numero:"))
conteggio=0
if num > 0:
    for i in range(10):
        i+=1
        x=int(input(f"{i}° numero:"))
        if x%num==0:
            conteggio+=1
print(f"Dei numeri che hai inserito, {conteggio} sono divisibili per {num}")

