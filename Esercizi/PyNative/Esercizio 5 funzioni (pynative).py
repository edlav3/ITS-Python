'''-- Crea una funzione esterna che accetterà due parametri a e b
-- Crea una funzione interna all'interno di una funzione esterna che calcolerà l'addizione di a e b
-- Infine, una funzione esterna aggiungerà 5 all'addizione e lo restituirà'''

def primaria(a:int, b:int):
    def secondaria(a:int, b:int):
        return a+b
    somma=secondaria(a, b)
    finale=terziaria(somma)
    return finale

def terziaria(valore:int):
    risultato=valore+5
    return risultato

x=int(input("Primo numero: "))
y=int(input("Secondo numero: "))
risultato=primaria(x, y)
print(f"{x}+{y}+5 = {risultato}")
