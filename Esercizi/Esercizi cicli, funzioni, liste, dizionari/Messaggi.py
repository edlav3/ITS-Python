'''crea un elenco contenente una serie di brevi messaggi di testo.
Passa l'elenco a una funzione chiamata show_messages(), che stampa ogni messaggio di testo.'''


list = ["Alessio", "Mario", "Valentino", "Mirko", "Alfio"]

def show_messages():
    for i in list:
            print(i)
show_messages()