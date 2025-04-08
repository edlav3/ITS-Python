'''Si supponga di voler calcolare l'ammontare del denaro depositato su un conto bancario ad interesse composto.
Se m è la somma depositata sul conto, la somma disponibile alla fine del mese sarà 1.005 volte m.
Scrivere una funzione ricorsiva compoundInterest che calcoli la somma presente sul conto dopo t mesi data una somma di partenza m.
'''

def compoundInterest(denaro:int, mesi:int) -> float:
    tassa=1.005
    if mesi==0:
        return denaro
    else:
        return tassa*compoundInterest(denaro, mesi-1)
    

print(compoundInterest(1000, 12))