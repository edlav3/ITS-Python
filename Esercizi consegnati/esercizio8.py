'''Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.

Esempio di output:
Se l'utente inserisce i numeri 5, 8, 3, 12, 7, il programma deve stampare:

*****
********
***
************
*******'''


print("Dammi 5 numeri compresi tra 1 e 30 (inclusi), stamperò righe contenenti tanti asterischi quanti il valore del numero dato")
i:int = 1
lista:list = []     # inizializzo variabile che scandisce i cicli e la lista che conterrà i valori dell'utente
while i<=5:
    num:int = int(input(f"{i}° numero: "))
    if num>=1 and num<=30:
        lista.append(num)
        i+=1         # fintanto che 'i' non è uguale a 5, chiedi all'utente un numero, se il numero soddisfa i requisiti inseriscilo dentro alla lista e aumenta 'i'
    else:
        print("Numero non valido")    # se non soddisfa i requisiti, stampa messaggio di errore e richiedi il numero

print("\n")
for i in range(len(lista)):
    print("*"*lista[i])     # stampa riga di asterishi tante volte quante il valore di 'lista[i]'