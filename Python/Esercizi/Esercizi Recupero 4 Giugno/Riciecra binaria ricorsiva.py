'''Implementa una funzione ricorsiva che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all'interno della lista, altrimenti False.'''



def ricerca(lista:list, num:int):
    mid=len(lista)//2
    if lista[mid]==num:
        print(f"Numero trovato in posizione {mid}")

    elif len(lista)==1:
        print("Numero non trovato")

    elif lista[mid]>num:
        ricerca(lista[:mid], num)
    
    elif lista[mid]<num:
        ricerca(lista[mid+1:], num)
