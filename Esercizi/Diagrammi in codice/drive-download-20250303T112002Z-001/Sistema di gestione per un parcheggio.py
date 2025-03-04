massimo=int(input("Quanti posti vuoi che abbia il parcheggio?"))
occupati=0
opzione = "ingresso"
while (opzione == "ingresso" or opzione == "uscita" or opzione == "stato" or opzione == "esci"):
    opzione=input("Digita:\n'ingresso' se vuoi occupare un nuovo posto\n'uscita' se vuoi liberare un posto\n'stato' se vuoi vedere lo stato del parcheggio\n'esci' se vuoi terminare il programma")
    if opzione == "ingresso":
        if occupati < massimo:
            occupati = occupati+1
            print(f"I posti occupati sono:\n{occupati}")
        else:
            print("Posti già tutti occupati")
    if opzione == "uscita":
        if occupati > 0:
            occupati = occupati-1
            print("I posti liberi sono:")
            print(massimo - occupati)
        else:
            print("Posti già tutti vuoti")
    if opzione == "stato":
        print(f"I posti occupati sono:\n{occupati}")
        print("I posti liberi sono:")
        print(massimo - occupati)
    if opzione == "esci":
        break