'''
I decorator sono funzioni che prendono in ingresso funzioni e restituiscono funzioni,
si chiamano decorator perchè la funzione restituita è costituita dalla funzione di input ma arricchita da qualcos'altro.
'''

def cronometro(fun): # 'fun' deve essere una funzione a sua volta
    def wrapper(): # inner function, funzione dentro un'altra funzione, il cuore del decorator si troverà qui dentro
        import time # l'import si può fare anche fuori
        start=time.time() # time.time() mi dice il tempo attuale
        fun() # fun rappresenta una funzione generica, alla funzione cronometro non interessa cosa faccia fun, ma per contare è necessario che venga eseguita al suo interno
        print(f"Tempo richiesto: {time.time() - start}") # viene stampato l'istante attuale (post-esecuzione di fun) - lo start iniziale
    return wrapper # ritorno la zona di memoria in cui si trova il wrapper

@cronometro # questa è la scrittura di un decorator --> decora la funzione che scrivo di seguito
# equivale a scrivere 'prova = cronometro (prova)'
def prova():
    lista=[]
    for i in range(100000000):
        lista.append(1)

prova() # quando l'interprete arriva a questa linea --> torna indietro a linea 6 --> esegue cronometro (perchè ho decorato prova()) -->
        # esegue il wrapper --> esegue fun() --> che nel nostro caso è 'prova()' --> stampa il tempo --> ritorna il wrapper.

        