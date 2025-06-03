'''Crea una funzione che prende un paragrafo e conta il numero di occorrenze di ogni parola.
La funzione dovrebbe stampare un rapporto che mostri le parole più frequenti e il loro numero di occorrenze.
È possibile utilizzare un ciclo for per eseguire l'iterazione sulle parole nel testo e un dizionario per memorizzare le occorrenze.
'''


def analisi(testo:str) -> dict[str:int]:
    risultato={}
    attuale=""
    i=0
    while i<len(testo):
        lettera=testo[i].lower()
        if "a" <= lettera <= "z":
            attuale+=lettera
        else:
            if attuale:
                if attuale in risultato:
                    risultato[attuale]+=1
                else:
                    risultato[attuale]=1
            attuale=""
        i+=1
    if attuale:
        if attuale in risultato:
            risultato[attuale]+1
        else:
            risultato[attuale]=1
    return risultato

x=analisi("Spesso il male di vivere ho incontrato: era il rivo strozzato che gorgoglia, era l'incartocciarsi della foglia riarsa, era il cavallo stramazzato.")
print(x)