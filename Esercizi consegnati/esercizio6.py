'''Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''


print("Dammi due numeri, calcolerò il prodotto dei numeri compresi")
prodotto=1
n1:int = int(input("Primo numero: "))
n2:int = int(input("Secondo numero: "))      # chiedo i numeri all'utente
if n1>n2:      # caso in cui il primo numero è maggiore del secondo
    i=n2       # i assume il valore del numero più piccolo trai due
    while i<=n1:
        prodotto*=i       # aggiorna variabile 'prodotto' fintanto che i non raggiunge il valore di n1 (come da condizione ciclo while)
        i+=1
else:         # caso in cui il secondo numero è maggiore del primo
    i=n1
    while i<=n2:
        prodotto*=i       # analogamente al primo caso, aggiorna 'prodotto' fintanto che i non raggiunge il valore di n2 (come da condizione ciclo while)
        i+=1
print(f"Il prodotto dei numeri compresi tra {n1} e {n2} è {prodotto}")
