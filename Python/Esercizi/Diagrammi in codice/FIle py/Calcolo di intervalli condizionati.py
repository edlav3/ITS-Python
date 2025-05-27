'''Progettare un algoritmo che chieda all'utente di inserire un valore intero n.
L'algoritmo deve:

Verificare se n è compreso tra 1 e 100:
se sì, calcolare e mostrare la somma di tutti i numeri pari compresi tra 1 e n.
Verificare se n è 0 o negativo:
Se sì, mostrare un messaggio di errore e terminare.
Altrimenti, calcolare e mostrare la somma di tutti i numeri dispari compresi tra 1 e n.'''


num=int(input("Inserisci un numero: "))
lista=[]
if num>0 and num<=100:
    for i in range(1, num+1):
        if i%2==0:
            lista.append(i)
    print(*lista, sep=', ')
elif num<=0:
    print("Numero non valido")
else:
    for i in range(100, num+1):
        if i%2!=0:
            lista.append(i)
    print(*lista, sep=', ')