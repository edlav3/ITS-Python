'''La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
Un errore nell'implementazione porta a risultati inaspettati.'''


def calculate_average(numbers: list[int]) -> float:
    somma=0
    if len(numbers) != 0:
        for i in numbers:
            somma+=i
        return somma/len(numbers)
    else:
        return 0
    

print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([]))