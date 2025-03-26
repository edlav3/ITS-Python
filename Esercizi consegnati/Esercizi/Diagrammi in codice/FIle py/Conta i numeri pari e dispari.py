'''Progetta un algoritmo che dati 10 numeri forniti dall'utente, conta quanti sono pari e quanti dispari.'''

contapari=0
contadispari=0
for i in range(10):
    x=int(input(f"{i+1}° numero:"))
    if x%2==0:
        contapari+=1 
    else:
        contadispari+=1
print(f"Dei numeri che hai fornito, {contapari} sono pari, {contadispari} sono dispari")