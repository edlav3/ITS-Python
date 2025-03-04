'''Progettare un algoritmo che consenta all'utente di inserire 10 numeri interi.
L'algoritmo deve:

contare quanti numeri sono positivi e quanti sono negativi,
verificare quanti numeri positivi sono pari e maggiori di 20,
verificare quanti numeri negativi sono dispari o minori di -10.
Mostrare in output i conteggi distinti per ogni categoria.'''


quantipositivi=0
quantinegativi=0
for i in range(1, 10):
    num=int(input(f"{i}° numero: "))
    if num>0:
        if num>20 and num%2==0:
            quantipositivi+=1
    elif num<0:
        if num<-10 or num%2!=0:
            quantinegativi+=1
    else:
        continue
print(f"I numeri positivi pari e maggiori di 20 sono {quantipositivi}")
print(f"I numeri numeri negativi dispari o minori di -10 {quantinegativi}")