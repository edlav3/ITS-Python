'''Scrivere un algoritmo che calcoli il valore di una sequenza numerica basata su un valore n inserito dall'utente. La sequenza segue queste regole:

se n è pari, calcolare la somma dei numeri da 1 a n che sono divisibili per 4;
se n è dispari, calcolare il prodotto dei numeri dispari da 1 a n;
se n è negativo, mostrare un messaggio di errore e terminare.
Infine, mostrare il risultato calcolato.'''


sommadiv4=0
prodottodis=1
num=int(input("Inserisci un numero: "))
if num%2==0:
    for i in range(1, num+1):
        if i%4==0:
            sommadiv4+=i
elif num%2!=0:
    for i in range(1, num+1):
        if i%2!=0:
            prodottodis=prodottodis*i
elif num<=0:
    print("Numero non valido")

if sommadiv4>0:
    print(f"La somma dei numeri da 1 a {num} che sono divisibili per 4 è {sommadiv4}")
if prodottodis>1:
    print(f"Il prodotto dei numeri dispari da 1 a {num} è {prodottodis}")