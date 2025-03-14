'''Progettare un algoritmo che richieda all’utente di inserire la sua età.
L'algoritmo deve:

controllare se l’età è compresa tra 18 e 65 anni.
Se sì, mostrare un messaggio che indica che l’utente può partecipare all’attività;

se l’età non rientra nell’intervallo, verificare se è inferiore a 18 oppure maggiore di 65.
Se sì, mostrare un messaggio che indica che l’utente non può partecipare perché ha superato l'età massima consentita
o non ha raggiunto l'età minima consentita.'''


anni = int(input("Quanti anni hai?"))
if anni>=18 and anni<=65:
    print("Età idonea")
elif anni<18:
    print("Mi spiace, non hai l'età minima per partecipare")
else:
    print("Mi spiace, età massima superata")