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