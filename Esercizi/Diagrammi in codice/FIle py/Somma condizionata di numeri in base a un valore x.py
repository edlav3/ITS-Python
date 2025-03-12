'''Progettare un algoritmo che chieda all'utente di inserire un valore x positivo. Se x è negativo,
l'algoritmo mostra un messaggio di errore e termina. Se x  è positivo, il programma deve consentire all'utente di inserire 10 numeri sia positivi che negativi. 

Se x è pari, allora dei numeri inseriti devono essere sommati solamente i numeri che sono maggiori della metà di x. 
Se, invece, x è dispari, dei numeri inseriti devono essere sommati solo i numeri che sono minori di x. 
'''

x = int(input("Dammi un numero\n"))
somma=0
if x>0:
   for i in range(10):
        num = int(input(f"{i+1}° numero:\n"))
        i=i+1
        if num % 2==0:
            if num>(x/2):
                somma=somma+num
            elif num<(x/2):
                somma=somma+num
else:
    print("Errore")
    
print(f"la somma è {somma}")