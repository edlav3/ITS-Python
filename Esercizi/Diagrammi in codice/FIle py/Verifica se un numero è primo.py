'''Progetta un algoritmo per determinare se un numero intero positivo inserito dall'utente è un numero primo'''

divisori=0
x=int(input("Inserisci un numero: "))
i=0
while i<x:
    i+=1
    if x%i==0:
        divisori+=1
if divisori>2:
    print(f"{x} non è un numero primo")
else:
    print(f"{x} è un numero primo")