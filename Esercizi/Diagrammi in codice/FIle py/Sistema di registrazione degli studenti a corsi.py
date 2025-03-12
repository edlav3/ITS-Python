massimo=100
occupati=0
risposta=""
nome_corso = input("Qual è il nome del corso?\n")
while risposta == "elimina" or "visualizza" or "annulla" or "iscrivi" or "esci":
    print("Digita:\n'iscrivi' se vuoi iscriverti al corso\n'annulla' se vuoi decrementare il numero di posti\n'visualizza' se vuoi vedere il numero di posti liberi\n'elimina' se vuoi cancellare il corso\n'esci' per terminare\n")
    risposta = input("")
    if risposta=="iscrivi":
        if occupati < massimo:
            occupati += 1
        else:
            print("Posti tutti occupati")
    if risposta == "annulla":
        if occupati>0:
            occupati -= 1
        else:
            print("Posti già tutti liberi")
    if risposta == "visualizza":
        liberi=massimo - occupati
        print(f"Per il corso {nome_corso} i posti occupati sono {occupati}, i posti liberi sono {liberi}\n")
    if risposta == "elimina":
        print("Ricominciamo allora\n")
        nome_corso = input("Qual è il nome del corso?\n")
    if risposta == "esci":
        print("Arrivederci allora")
        break