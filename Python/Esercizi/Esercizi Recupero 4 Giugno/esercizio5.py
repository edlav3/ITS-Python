'''Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold'''

def funzione(lista:list[int], threshold:int) -> list[int]:
    nuova=[]
    for num in lista:
        if num<=threshold:
            num*=3
            nuova.append(num)
        else:
            nuova.append(num)
    return nuova

lista=[1, 4, 56, 7, 5, 3]
print(funzione(lista, 9))