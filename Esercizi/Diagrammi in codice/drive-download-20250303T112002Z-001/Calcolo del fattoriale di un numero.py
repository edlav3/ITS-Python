while True:
    n=int(input("Dammi un numero, calcolerò il fattoriale: "))
    if n<0:
        print("Numero non valido")
    else:
        break
fattoriale=1
for i in range(1, n+1):
    fattoriale*=i
print(f"Il fattoriale di {n} è: {fattoriale}")