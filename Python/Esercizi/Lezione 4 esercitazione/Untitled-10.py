'''Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.'''


def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    nuovo=dict1
    for chiave in dict2:
        if chiave not in nuovo:
            nuovo[chiave]=dict2[chiave]
        else:
            nuovo[chiave]=dict1[chiave]+dict2[chiave]
    return nuovo
        
            


print(merge_dictionaries({'x': 5}, {'x': -5}))