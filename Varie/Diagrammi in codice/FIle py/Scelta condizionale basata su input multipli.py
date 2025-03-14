'''Progettare un algoritmo che richieda all’utente di inserire un numero variabile n di valori x e y. L'algoritmo deve:

calcolare il prodotto di x e y solo se entrambi i valori sono positivi;
calcolare la somma di x e y solo se uno dei due valori è negativo;
mostrare il risultato dell’operazione effettuata o un messaggio di errore altrimenti.'''

coppie=int(input("Quante coppie di numeri vuoi inserire?"))
somma=0
prodotto=1
for i in range(coppie):
    i+=1
    x=int(input(f"{i}° valore x:"))
    y=int(input(f"{i}° valore y:"))
    if x>0 and y>0:
       prodotto=x*y
       print(f"Il prodotto tra x e y è {prodotto}")
    elif x<0 or y<0:
        somma=x+y
        print(f"La somma tra x e y è {somma}")
    else:
        print("Errore")