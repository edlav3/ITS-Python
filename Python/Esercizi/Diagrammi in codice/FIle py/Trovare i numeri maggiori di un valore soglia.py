'''Progetta un algoritmo che dati 7 numeri, trova e comunica i numeri maggiori di un valore soglia fornito dall'utente.'''

soglia=int(input("Inserisci un numero"))
quanti=0
print("Ora inserisci 7 numeri")
for i in range(7):
    num=int(input(f"{i+1}° numero"))
    if num>soglia:
        quanti+=1
print(f"Dei numeri che hai inserito, quelli che superano {soglia} sono {quanti}")