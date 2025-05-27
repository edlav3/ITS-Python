'''Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.'''


def somma_elementi(x:list, y:list):
    nuova=[]
    if len(x)!=len(y):
        return nuova
    else:
        for i in range(len(x)):
            somma=x[i]+y[i]
            nuova.append(somma)
        return nuova

print(somma_elementi([1,1,1],[1,1,1]))