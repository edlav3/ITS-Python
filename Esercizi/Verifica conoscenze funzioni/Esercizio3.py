'''Scrivi una funzione che calcoli i fattori primi di un numero intero positivo n.
Un fattore primo di n è un numero primo che divide esattamente n (cioè senza resto), e la cui moltiplicazione in sequenza restituisce n.
Un numero può avere lo stesso fattore primo più volte.'''



def prime_factors(num:int):
    divisore=2
    fattori=[]
    while True:
        if num%divisore==0:
            fattori.append(divisore)
            num=num//divisore
        else:
            divisore+=1
        if num==1:
            break
    return fattori

print(prime_factors(4))