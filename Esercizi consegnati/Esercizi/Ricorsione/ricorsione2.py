'''Scrivi una funzione sumInRange che calcoli la somma di tutti gli interi tra a e b, inclusi, dove a e b vengono passati come
input alla funzione.
Per risolvere l'esercizio, è obbligatorio usare un ciclo while e si presume che il valore di b sia sempre maggiore del
valore di a. Pertanto, se a > b, è necessario scambiare i valori per garantire che a sia il più piccolo dei due.
Infine, è consentito dichiarare solo una variabile, oltre ai parametri della funzione, per memorizzare la somma.
Quindi, chiama la funzione sumInRange per a = 5, b = 10 e per a = 10, b = 5.'''

def suminrange(a:int, b:int) -> int:
    somma=0
    temp=0
    if a>b:
        temp=b
        b=a
        a=temp
    while a<=b:
        somma+=a
        a+=1

    return somma

print(suminrange(5, 10))


'''Scrivi una funzione ricorsiva recursiveSumInRange che calcoli la somma di tutti gli interi tra a e b, inclusi, dove a e b vengono passati come input alla funzione.
Supponiamo che il valore di b sia sempre maggiore del valore di a. Pertanto, se a > b, è necessario scambiare i valori per
assicurarsi che a sia il più piccolo dei due.
Quindi, chiama la funzione recursiveSumInRange per a = 5, b = 10 e per a = 10, b = 5.'''


def recursiveSumInRange(a:int, b:int) -> int:
# if a > b, swap values of a and b
    if a > b:
# define a temporary variable called temp, containing value of a
        temp:int = a
# swap values of a and b
        a = b
        b = temp # now b = a
# if b = a, the recursive process must be stopped
    if b == a:
        return int(a)
# otherwise, compute the sum recursively
    else:
        return int(b + recursiveSumInRange(a, b-1))
    
print(recursiveSumInRange(5, 10))