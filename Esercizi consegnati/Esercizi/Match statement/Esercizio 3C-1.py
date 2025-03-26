'''Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana.
Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:

- 10 → "Eccellente"
- 8-9 → "Molto buono"
- 6-7 → "Sufficiente"
- 4-5 → "Insufficiente"
- 1-3 → "Gravemente insufficiente"
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto: 5
Output: Insufficiente
- - - - - - - - - - -
Inserisci il voto: 11
Output: Voto non valido'''


voto=float(input("Inserisci il voto: "))
match voto:
    case voto if voto>=1 and voto<=3:
        print("Voto gravemente insufficiente")
    case voto if voto>=4 and voto<=5:
        print("Insufficiente")
    case voto if voto>=6 and voto<=7:
        print("Sufficiente")
    case voto if voto>=8 and voto<=9:
        print("Molto buono")
    case 10:
        print("Eccellente")
    case voto if voto%0.25!=0:
        print("Voto non valido, sono ammessi solo due numeri dopo la virgola")
    case _:
        print("Voto non valido")