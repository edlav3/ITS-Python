'''Scrivi un programma per creare una funzione ricorsiva per calcolare la somma dei numeri da a a b, dove a e b sono dati in input.

Una funzione ricorsiva è una funzione che richiama se stessa più e più volte.

Risultato atteso:

55'''

def ricorsiva(a:int, b:int):
    somma=0
    if a>b:
        differenza=a-b
        for i in range(b, differenza+1):
            somma+=i
    elif b>a:
        differenza=b-a
        for i in range(a, differenza+1):
            somma+=i
    else:
        somma=0

    return somma


x=int(input("Primo numero: "))
y=int(input("Secondo numero: "))
somma=ricorsiva(x, y)
print(somma)