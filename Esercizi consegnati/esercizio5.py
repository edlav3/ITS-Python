'''Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna.
Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:

Acquisisca in input un valore N (numero di euro disponibili).
Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
Mostri quanti buoni sconto avanzano al termine dell'acquisto.'''



print("Vuoi una barretta di ciccolato? Ogni 6 barrette ne hai una omaggio, una barretta costa 1€")
euro = float(input("Quanti soldi hai?"))
omaggio:int = euro//6        # divisione intera per scandire quante sono le barrette omaggio
mancanti:int = euro%6        # modulo tra 'euro' e 6 per stabilire quanti sono i buoni che avanzano
prossima=6-mancanti    # differenza tra 6 e 'mancanti' per sapere quanti buoni servono per accedere alla prossima barretta omaggio
print(f"Puoi acquistare {(euro + omaggio):.0f} barrette di cui {omaggio:.0f} sono omaggio\nAvanzano {mancanti:.0f} buoni, compra altre {prossima:.0f} barrette per avererne un'altra omaggio")