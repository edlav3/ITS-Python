'''Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall'utente.

Il programma deve:

acquisire una sequenza di numeri interi, terminando l'inserimento quando l'utente digita 0 (che non deve essere considerato nei calcoli);
calcolare e visualizzare la somma di tutti i numeri pari inseriti;
calcolare e visualizzare la media di tutti i numeri dispari inseriti;
determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
Esempio di input e output
Input:

Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 2
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 3
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 0
Output:

Somma dei numeri pari: 10
Media dei numeri dispari: 5.67
Numero più frequente: 7 (2 volte)'''


num:int = 1
sommapari:int = 0
sommadispari:int = 0
mediadispari:int = 0
quantidispari:int = 0
numeri:list = []        # dichiaro le varibili necessarie
while num!=0:         # fintanto che il numero inserito è diverso da 0...
    num=int(input("Inserisci un numero (0 per terminare): "))
    numeri.append(num)    # ... inserisci il numero dentro una lista
    if num==0:
        break
    elif num%2==0:
        sommapari+=num      # se il numero è pari aggiungilo alla somma
    elif num%2!=0:          # se è dispari fanne la media
        sommadispari+=num
        quantidispari+=1
        mediadispari=sommadispari/quantidispari


print(f"Somma dei numeri pari: {sommapari}\nMedia dei numeri dispari: {mediadispari:.2f}")


frequenza:int = 0
fmassima:int = 0
valori=[]
for i in range(len(numeri)):
    frequenza=numeri.count(numeri[i])      # per ogni valore della lista, utilizza funzione 'count' per vedere quante volte compare e memorizzalo dentro ad una variabile
    if fmassima<frequenza:
        fmassima=frequenza           # verifica che la frequenza del 'i-esimo' numero sia maggiore di tutte le altre



print(f"Il numero più frequente è stato scritto {fmassima} volte")