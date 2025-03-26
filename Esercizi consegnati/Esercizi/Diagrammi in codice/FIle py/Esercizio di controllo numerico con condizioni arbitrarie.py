'''Progettare un algoritmo che verifichi se tre numeri interi positivi x, y, z rispettano le seguenti regole:

la somma di x+y+z deve essere pari;
x deve essere divisibile per 3, y divisibile per 5 e z divisibile per 7;
se entrambe le condizioni sono vere, mostrare: “Regole rispettate”. Altrimenti, mostrare: “Regole non rispettate”.'''


x=int(input("Valore x:"))
y=int(input("Valore y:"))
z=int(input("Valore z:"))
if (x%1==0 and x>0 and y%1==0 and y>0 and z%1==0 and z>0):
    if (x+y+z)%2==0 and x%3==0 and y%5==0 and z%7==0:
        print("Regole rispettate")
    else:
        print("Regole non rispettate")
else:
    print("Uno dei numero è negativo o non intero")