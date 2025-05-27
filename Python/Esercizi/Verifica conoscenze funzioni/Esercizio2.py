'''Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:

tutti i numeri pari vengano prima di tutti i numeri dispari;

l’ordine relativo tra pari e dispari va mantenuto;

l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi.'''


def even_odd_pattern(lista:list):
    nuova=[]
    indice=0
    for i in lista:
        if i%2==0:
            nuova.insert(indice, i)
            indice+=1
        elif i%2!=0:
            nuova.insert(len(lista), i)
    return nuova

print(even_odd_pattern([3, 6, 1, 8, 4, 7]))