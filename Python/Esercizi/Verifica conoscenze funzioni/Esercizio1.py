'''Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, dove n è la lunghezza della lista.
Tuttavia, alcuni numeri potrebbero mancare: la lista può contenere duplicati, ma non tutti i numeri da 1 a n sono presenti.
Il tuo compito è individuare i numeri mancanti.
Scrivi una funzione che, data in input una lista, restituisca una nuova lista ordinata contenente
tutti i numeri da 1 a n che non sono presenti nella lista originale.'''

'''Test print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))
Result [5, 6]'''

def find_disappeared_numbers(lista:list):
    nuova=[]
    maggiore=-99999999999
    minore=999999999999
    attuale=0
    for i in lista:
        if i>maggiore:
            attuale=i
            nuova.append(i)
        elif i<minore:
            minore=i
            nuova.append(i)
        return nuova

lista=[6,4,3,6,89,3,1,5]
prova=find_disappeared_numbers(lista)
print(prova)
