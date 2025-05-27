'''crea un dizionario chiamato città. Usa i nomi di tre città come chiavi nel tuo dizionario.
Crea un dizionario di informazioni su ogni città e includi il paese in cui si trova la città,
la sua popolazione approssimativa e un fatto su quella città. Le chiavi per il dizionario di ogni città dovrebbero essere qualcosa come paese,
popolazione e fatto. Stampa il nome di ogni città e tutte le informazioni che hai memorizzato su di essa.'''



città={"Montecarlo": {"Abitanti": 33000, "Paese": "Francia", "Fatto": "Ha il casino più lussuoso del mondo"},
       "Rimini": {"Abitanti": 150000, "Paese": "Italia", "Fatto": "Ci ho perso il telefono nel 2022"}, 
       "Cracovia": {"Abitanti": 790000, "Paese": "Polonia", "Fatto": "Meta ideale per le vacanze natalizie"}}

for nomi, dati in città.items():
    print(f"\nCittà: {nomi}")
    for chiave, valore in dati.items():
        print(f"{chiave}: {valore}")