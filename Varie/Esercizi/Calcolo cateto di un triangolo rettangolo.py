'''Progetta un algoritmo per ottenere la misura di un cateto c in un triangolo rettangolo,
conoscendo quelle dell’ipotenusa a e dell’altro cateto b.'''

ipotenusa=int(input("Misura dell'ipotenusa:"))
cateto1=int(input("Misura del cateto:"))
cateto2=(ipotenusa**2-cateto1**2)**(1/2)
print(f"Il secondo cateto misura {cateto2:.2f}")