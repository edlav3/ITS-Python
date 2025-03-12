'''Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale.
Il programma deve poi visualizzare la stringa ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''



stringa:str = str(input("Posso invertire i caratteri che inserisci, scrivi qualcosa!"))
invertita:str = ""      # definisco una stringa vuota che andrà a contenere i caratteri invertiti
i=len(stringa)
while i > 0:        # fintanto che i è maggiore di 0...
    i -= 1
    invertita+=stringa[i]    # ... decrementa i e inserisci il i-esimo carattere dentro la stringa di nome 'invertita'
print(f"La stringa invertita è:\n{invertita}")