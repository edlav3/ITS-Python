'''Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.'''


x=int(input("Dammi un numero: "))
if x%2==0:
    risultato=x//2
else:
    risultato=x*3-1

print(risultato)