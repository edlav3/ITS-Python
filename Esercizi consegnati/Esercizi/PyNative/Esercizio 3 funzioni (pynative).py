'''Scrivi un programma per creare una funzione calculation() tale che possa accettare due variabili e calcolare addizione e sottrazione.
Inoltre, deve restituire sia addizione che sottrazione in una singola chiamata di ritorno .'''


def calculation(a:int, b:int):
    somma=a+b
    differenza=a-b 

    return somma, differenza


a=int(input("Primo numero: "))
b=int(input("Secondo numero: "))
risultati=calculation(a, b)
print(f"La somma tra i due numeri è {risultati[0]} la differenza tra {a} e {b} è {risultati[1]}")