'''Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi.
Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.'''


def count_isolated(numbers:list) -> int:
    count=0
    if numbers[0]!=numbers[1]:
        count+=1
    for i in range(1,len(numbers)-1):
        if numbers[i]!=numbers[i-1] and numbers[i]!=numbers[i+1]:
            count+=1
    if numbers[len(numbers)-1]!=numbers[len(numbers)-2]:
         count+=1
    return count

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(count_isolated([1, 2, 3, 4, 5]))
