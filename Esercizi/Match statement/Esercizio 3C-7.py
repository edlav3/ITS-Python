'''Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".'''


testa=0
croce=0
i=1
while i<=8:
    lancio=str(input(f"Lancio della {i}° moneta ('t' o 'T' per testa, 'c' o 'C' per croce): "))
    match lancio:
        case "t"|"T":
            testa+=1
            i+=1
        case "c"|"C":
            croce+=1
            i+=1
        case _:
            print("Lancio non valido, si prega di ritirare")

percentualetesta=(testa/8)*100
percentualecroce=(croce/8)*100
print(f"Hai lanciato 8 dadi, {testa} volte è uscito testa con il {percentualetesta:.2f}%, {croce} volte è uscito croce con il {percentualecroce:.2f}%")