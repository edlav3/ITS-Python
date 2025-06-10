'''Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all'interno della lista, altrimenti False.'''


def ricerca(lista:list[int], ricercato:int) -> bool:
    nuova=[]
    for i in range(len(lista)):
        attuale=lista[i]
        if attuale<lista[i]:
            nuova.insert(0,lista[i])
        else:
            nuova.append(lista[i])
    inizio=0
    fine=len(nuova)-1
    while inizio<=fine:
        circaMeta=(inizio+fine)//2
        if nuova[circaMeta]==ricercato:
            return True
        elif nuova[circaMeta]>ricercato:
            fine=circaMeta-1
        else:
            inizio=circaMeta+1
    return False

lista=(1,4,5,6,2,3,56)
print(ricerca(lista, 57))