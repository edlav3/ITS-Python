'''Progettare un algoritmo che chieda all’utente di inserire due valori interi positivi 𝐴 e 𝐵 con 𝐴 < 𝐵.
Se i valori non rispettano le condizioni, mostrare un messaggio di errore e terminare.
Se i valori sono validi, calcolare la somma di tutti i numeri interi compresi tra 𝐴 e 𝐵 (inclusi) e mostrare il risultato.'''

print("Il secondo numero deve essere maggiore del primo, entrambi devono essere positivi e interi")
differenza=0
a = int (input("Primo numero:"))
somma=0
b = int (input("Secondo numero:"))
if (a<0 and a%1!=0 and b<0 and b%1!=0):
    print("Valori non valido")
elif a<b:
    differenza=b-a
    i=a
    for index in range(differenza+1):
        somma+=i
        i+=1
    print(f"La somma dei valori compresi tra {b} e {a} è {somma}")
else:
    print(f"{b} è minore o uguale a {a}")