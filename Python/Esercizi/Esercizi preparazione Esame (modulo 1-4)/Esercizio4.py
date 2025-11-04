'''Scrivi una funzione che converta una lista di tuple (chiave, valore)
in un dizionario. Se la chiave è già presente,
aggiungi il valore alla lista di valori già associata alla chiave.'''

def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    dizionario={}
    for key, value in tuples:
        if key in dizionario:
            dizionario[key].append(value)
        else:
            dizionario[key]=[value]
    return dizionario