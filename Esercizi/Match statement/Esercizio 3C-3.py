'''Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:

- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"

Expected Output:

['casa', 'hotel', 'b&b']
Categoria sconosciuta

--------------------------

['penna', 'matita', 'quaderno']
Materiale scolastico'''


oggetti=[]
i=1
while i<=3:
    oggetto=str(input("Inserisci un oggetto: "))
    i+=1
    oggetti.append(oggetto)

conteggio=0
for i in range(3):
    x=oggetti[i]
    match x:
        case x if x in ["penna", "matita", "quaderno"]:
            conteggio+=1
            if conteggio==3:
                print("Materiale scolastico")
        case x if x in ["pane", "latte", "uova"]:
            conteggio+=1
            if conteggio==3:
                print("Prodotti alimentari")
        case x if x in ["sedia", "tavolo", "armadio"]:
            conteggio+=1
            if conteggio==3:
                print("Mobili")
        case x if x in ["telefono", "computer", "tablet"]:
            conteggio+=1
            if conteggio==3:
                print("Dispositivi elettronici")
        case _:
            print("Oggetti non riconosciuti")
        