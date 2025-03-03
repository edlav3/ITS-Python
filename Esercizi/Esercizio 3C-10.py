'''Scrivere un programma in Python che permetta all'utente di inserire una data
(giorno e mese espressi in forma numerica),
salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."

Expected Output:

Inserisci il giorno: 25
Inserisci il mese: 12
Output: Il 25/12 è Natale!

- - - - - - - - - - - - - - -

Inserisci il giorno: 5
Inserisci il mese: 3
Output: Nessuna festività importante in questa data.'''


giorno:int = int(input("Inserisci il giorno: "))
mese:int = int(input("Inserisci il mese: "))
data=(giorno, mese)

if giorno<=31 and giorno>=1 and mese<=12 and mese>=1:
    match data:
        case data if giorno==1 and mese==1:
            print("Capodanno")
        case data if giorno==14 and mese==2:
            print("San Valentino")
        case data if giorno==2 and mese==6:
            print("Festa della Repubblica")
        case data if giorno==15 and mese==8:
            print("Ferragsto")
        case data if giorno==31 and mese==10:
            print("Halloween")
        case data if giorno==25 and mese==12:
            print("Natale")
        case _:
            print("Nessuna festività importante in questa data")
else:
    print("Data non valida")