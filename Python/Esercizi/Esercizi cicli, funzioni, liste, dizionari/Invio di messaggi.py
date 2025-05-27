'''Scrivi una funzione chiamata send_messages() che stampa ogni messaggio di testo e sposta ogni messaggio
in una nuova lista chiamata sent_messages mentre viene stampata. Dopo aver chiamato la funzione,
stampa entrambe le tue liste per assicurarti che i messaggi siano stati spostati correttamente.'''


lista = ["Alessio", "Mario", "Valentino", "Mirko", "Alfio"]

sent_message=[]

def send_messages():
    for i in lista:
            print(i)
            sent_message.append(i)

send_messages()
print(sent_message)