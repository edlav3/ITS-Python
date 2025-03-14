'''Progettare un algoritmo che richieda all’utente di inserire un valore intero.
Il programma deve verificare:

se il numero è pari e maggiore di 10. Se sì, mostrare “Numero valido”;
se il numero è dispari o minore o uguale a 10. Se sì, mostrare “Numero non valido”.'''

num=int(input("Dammi un numero intero:"))
if num%2==0 and num > 10:
    print("Numero valido")
else:
    print("Numero non valido")