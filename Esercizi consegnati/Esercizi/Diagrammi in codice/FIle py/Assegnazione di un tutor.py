'''Progettare un algoritmo che assegni i 10 tutor disponibili agli studenti che necessitano di recupero in un istituto scolastico.
Per ogni studente dato in input, il sistema deve controllare la disponibilità dei tutor e, nel caso di disponibilità, assegnarlo allo studente.
Se il numero di tutor disponibili scende a zero, occorre aumentare il numero di studenti in lista d'attesa.
Occorre confermare sia l’assegnazione del tutor con successo che l'inserimento nella lista d’attesa allo studente.
L'algoritmo termina solo quando il numero di tutor è pari a 0 e la lista d'attesa conta 50 studenti.'''


tutor = 10
attesa = 0
studenti = 0
avanti = "si"
while avanti == "si":
    avanti = input("Scrivi 'si' per inserire nuovo studente")
    if avanti == "si":
        tutor -= 1
        studenti += 1
        if tutor >= 0:
            print("Tutor assegnato correttamente")
        if tutor < 0:
            attesa += 1
            print("Inserito in lista d'attesa")
            if attesa >= 50:
                print("Lista piena")
                break
print(f"Studenti in attesa: {attesa}, studenti gestiti: {studenti}")