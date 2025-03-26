num = int(input("Dammi un numero\n"))
if num > 0:
    risultato=0
    i=0
    for i in range(num+1):
        risultato=risultato+i*i
        i=i+1
    print(f"Il risultato è {risultato}")
else:
    print("Errore")
    
