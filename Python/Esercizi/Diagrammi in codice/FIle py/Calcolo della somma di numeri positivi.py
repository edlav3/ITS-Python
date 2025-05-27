'''Progettare un algoritmo che calcoli la somma dei soli numeri positivi tra 5 valori inseriti dall'utente.
Quindi, se un numero è negativo o zero, ignora quel valore nella somma.'''

somma=0
for i in range(1, 6):
    x=int(input(f"{i}° numero: "))
    if x>0:
        somma+=x
print(f"La somma dei valori positivi è: {somma}")