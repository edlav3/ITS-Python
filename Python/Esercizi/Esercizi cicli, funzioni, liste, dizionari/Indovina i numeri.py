'''Creare una funzione che generi un numero casuale all'interno di un intervallo specificato dall'utente.
Richiedi all'utente di indovinare il numero entro un numero massimo specificato di tentativi.
Fornire feedback all'utente dopo ogni ipotesi, indicando se la sua ipotesi è troppo alta, troppo bassa o corretta.
Terminare il ciclo quando l'utente indovina correttamente il numero o raggiunge il numero massimo di tentativi.'''

import random

def randomNum(min:int, max:int):
    num=random.randint(min, max)
    return num

def indovinare(minimo:int, massimo:int, tentativi: int):
    unNumero=randomNum(minimo, massimo)
    for x in range(tentativi):
        numeroUt=int(input("Dammi un numero "))
        if numeroUt==unNumero:
            print("Indovinatooo")
            break
        elif numeroUt>unNumero:
            print("Numero troppo grande")
            print(f"Tentativi rimanenti: {tentativi-(x+1)}")
        else:
            print("Numero troppo piccolo")
            print(f"Tentativi rimanenti: {tentativi-(x+1)}")


minimo=int(input("Minimo: "))
massimo=int(input("Massimo: "))
tentativi=int(input("Tentativi: "))
indovinare(minimo, massimo, tentativi)