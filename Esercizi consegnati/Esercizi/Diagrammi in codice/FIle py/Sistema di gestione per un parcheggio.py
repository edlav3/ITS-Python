posti=int(input("Quanti posti vuoi che abbia il parcheggio? "))
occupati=0
while True:
    opzione=input("\nDigita:\n'ingresso' se vuoi occupare un nuovo posto\n'uscita' se vuoi liberare un posto\n'stato' se vuoi vedere lo stato del parcheggio\n'esci' se vuoi terminare il programma\n")
    if opzione == "ingresso":
        if occupati < posti:
            occupati = occupati+1
            print(f"I posti occupati sono: {occupati} su {posti}")
        else:
            print("Posti già tutti occupati")
    elif opzione == "uscita":
        if occupati > 0:
            occupati = occupati-1
            print("Posto liberato")
            print(f"Ora i posti liberi sono: {posti - occupati} su {posti}")
        else:
            print("Posti già tutti vuoti")
    elif opzione == "stato":
        print(f"I posti occupati sono {occupati}")
        print(f"I posti liberi sono: {posti - occupati}\nI posti in totale sono {posti}")
    elif opzione == "esci":
        print("Arrivederci")
        break
    else:
        print("Risposta non valida")