'''Progetta un algoritmo per ottenere la misura di un cateto c in un triangolo rettangolo,
conoscendo quelle dell’ipotenusa a e dell’altro cateto b.'''

a=float(input("Misura dell'ipotenusa: "))
b=float(input("Misura del cateto: "))
if a>b:
    c=(a**2-b**2)**(1/2)
    print(f"Il secondo cateto misura {c:.2f}")
else:
    print("Errore")