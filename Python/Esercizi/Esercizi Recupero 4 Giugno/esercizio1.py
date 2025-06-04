'''Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.'''


def convertitore(lista:list[tuple]) -> dict:
    dizionario={}
    for tupla in lista:
        if tupla[0] not in dizionario:
            dizionario[tupla[0]]=tupla[1]
        else:
            dizionario[tupla[0]]+=tupla[1]
    return dizionario


lista=[("ciao", 5), ("ciao", 6), ("mario", 4)]
print(convertitore(lista))