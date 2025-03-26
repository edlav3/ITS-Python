'''Scrivere un algoritmo che consenta all'utente di inserire una numero variabile di numeri interi (la quantità è scelta dall'utente). L'algoritmo deve:

sommare i numeri pari e maggiori della media dei numeri inseriti fino a quel momento;
sommare i numeri dispari o minori della media dei numeri inseriti fino a quel momento;
Mostrare in output entrambe le somme e indicare quale somma è maggiore.'''

somma=0
media=0
quantimaggiori=0
quantiminori=0
quanti=int(input("Quanti numeri vuoi inserire: "))
if quanti>0:
    for i in range(1, quanti+1):
        num=int(input(f"{i}° numero: "))
        somma+=num
        media=somma/i
        if num>media and num%2==0:
            quantimaggiori+=1
        elif num<media and num%2!=0:
            quantiminori+=1
        else:
            continue
massimo=0
if quantimaggiori>quantiminori:
    massimo=quantimaggiori
else:
    massimo=quantiminori

print(f"Numeri pari e maggiori della media: {quantimaggiori},\nNumeri dispari e minori della media: {quantiminori},\nIl valore più grande tra i due è {massimo}")