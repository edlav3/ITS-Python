'''Scrivi una funzione che, data una lista, ritorni un dictionary
che mappa ogni elemento alla sua frequenza nella lista.'''

def frequency_dict(elements: list) -> dict:
    dizionario={}
    for x in elements:
        if x in dizionario:
            dizionario[x]+=1
        else:
            dizionario[x]=1
    return dizionario