''' Crea una funzione che prenda come input il nome di uno studente e i suoi punteggi in diverse materie.
La funzione calcola il punteggio medio e stampa il nome, la media e un messaggio dello studente indicando se lo studente ha superato l'esame (media >= 60) o non è riuscito.
Creare un ciclo for da ripetere su un elenco di studenti e punteggi, chiamando la funzione per ogni studente.'''

def funzione1(**diz):
    for key, value in diz.items():
        somma = sum(value)
        media=somma/len(value)
        if media>=60:
            print(f"Complimenti {key}! Esame superato")
        else:
            print(f"Peccato {key}. Esame non superato")


funzione1(Mario=[70, 65, 80], Lucia=[50, 40, 55])
funzione1(Anna=[60, 60, 60])
