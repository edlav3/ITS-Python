'''Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere,
ritorni un nuovo insieme senza i numeri specificati nella lista.'''


def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    insieme=list(original_set) - (elements_to_remove)
    return insieme

print(remove_elements({5, 6, 7}, [7, 8, 9]))
