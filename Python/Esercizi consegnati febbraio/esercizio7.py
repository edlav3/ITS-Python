'''Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

Esempio:

a[1] + b[n-1], a[2] + b[n-2], ...

Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c.'''

a:list =[300, 5, 7, 10, 15]
b:list =[5, 5, 8, 11, 700]
c:list =[]
somma:int =0
index_a:int =0
index_b:int =len(b)-1      # dichiaro le variabili
while index_a<len(a) and index_b>=0:
    somma=a[index_a]+b[index_b]
    index_a+=1         # indice di a scorre in avanti fino a quando non è uguale alla lunghezza della lista (come da condizione while)
    index_b-=1         # indice di b scorre all'idietro fino a quando non è uguale a 0 (come da condizione while)
    c.append(somma)
print(f"La somma incrociata delle liste:\na:{a}\nb:{b}\nHa come risultato la lista c: {c}")