'''Progetta un algoritmo per gestire la prenotazione dei posti in una sala che contiene 20 sedie libere.
L'utente può inserire una delle seguenti opzioni "prenota", "libera", "visualizza", "esci". Per ogni opzione:

se l'utente inserisce "prenota", se ci sono ancora sedie libere, decrementa di uno il numero di posti liberi;
se l'utente inserisce "libera", incrementa di uno il numero di sedie libere;
se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati;
se l'utente inserisce "esci", termina l'algoritmo.
Torna all'inserimento di una opzione finché l'utente non seleziona "esci".'''

print("Ti permetterò di gestire la prenotazione dei posti in una sala che contiene 20 sedie libere.")
libere=20
occupate=0
esito=str(input("Digita:\n'prenota' per prenotare un posto,\n'libera' per liberare un posto,\n'visualizza' per vedere lo stato dei posti,\n'esci' per terminare: "))
while esito!="esci":
    if esito=="prenota":
        if libere>0:
            libere-=1
            occupate+=1
            print("Sedia prenotata correttamente")
        else:
            print("\nSedie tutte occupate\n")
    elif esito=="libera":
        if libere<20:
            libere+=1
            occupate-=1
            print("Sedia liberata correttamente")
        else:
            print("\nSedie già tutte libere\n")
    elif esito=="visualizza":
        print(f"\nLe sedie occupate sono {occupate}, le sedie libere sono {libere}\n")
    else:
        print("Risposta non valida")

    esito=str(input("Digita:\n'prenota' per prenotare un posto,\n'libera' per liberare un posto,\n'visualizza' per vedere lo stato dei posti,\n'esci' per terminare: "))

print("Buona giornata!")