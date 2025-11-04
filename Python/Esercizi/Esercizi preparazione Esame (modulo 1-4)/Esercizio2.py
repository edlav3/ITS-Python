'''Scrivi una funzione che prende una lista di numeri
e ritorna un dizionario che classifica i numeri in liste
separate per numeri pari e dispari.
'''

def classifica_numeri(lista: list[int]) -> dict[str:list[int]]:
    pari=[]
    dispari=[]
    for i in lista:
        if i%2==0:
            pari.append(i)
        else:
            dispari.append(i)
    dizionario={"pari":pari, "dispari":dispari}
    return dizionario
    