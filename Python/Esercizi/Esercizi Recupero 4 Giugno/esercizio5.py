'''Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold'''

def funzione(lista:list[int], threshold:int) -> list[int]:
    totale=1
    for num in lista:
        if num<=threshold:
            totale*=num
    return totale

lista=[1, 4, 56, 7, 5, 3, 6, 11]
print(funzione(lista, 9))