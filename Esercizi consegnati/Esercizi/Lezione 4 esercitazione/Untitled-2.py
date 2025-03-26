'''Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.'''

def list_statistics(numbers: list[int]) -> tuple[int]:
    massimo=-9999999999
    minimo=999999999
    somma=0
    for i in numbers:
        if i<minimo:
            minimo=i
        if i>massimo:
            massimo=i
    
    for i in numbers:
        somma+=i

    media=somma/(len(numbers))
    risultati=(massimo, minimo, media)
    return risultati

print(list_statistics([1, 2, 3, 4, 5]))

