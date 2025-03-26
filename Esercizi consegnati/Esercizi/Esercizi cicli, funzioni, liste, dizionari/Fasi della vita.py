
age=int(input("Quanti anni hai?"))
if age<0:
    print("Età non valida")
else:
    if age<2:
        print("Neonato")
    elif age>=2 and age<=4:
        print("Bambino")
    elif age>4 and age<=13:
        print("Bambino cresciuto")
    elif age>13 and age<=20:
        print("Adolescente")
    elif age>20 and age<=65:
        print("Adulto")
    else:
        print("Anziano")