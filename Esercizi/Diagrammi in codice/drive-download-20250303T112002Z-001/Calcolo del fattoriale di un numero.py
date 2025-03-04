x=int(input("Dammi un numero:"))
fattoriale=1
i=x
while i>1:
    fattoriale=fattoriale*i
    i=i-1
print(f"Il fattoriale di {x} è {fattoriale}")