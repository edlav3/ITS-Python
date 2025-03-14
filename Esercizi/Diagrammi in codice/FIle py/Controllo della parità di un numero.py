'''Progetta un algoritmo utile a determinare se un numero inserito dall'utente è pari o dispari'''

i=0
x=int(input("Inserisci un numero:"))
if x%2==0:
    print(f"{x} è pari")
else:
    print(f"{x} è dispari")