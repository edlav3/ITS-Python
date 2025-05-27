'''Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

Suggerimento: ogni volta che si effettua una chiamata ricorsiva, si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri compresi tra il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.'''



def vowelCounter(stringa:str):
    vocali=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if not stringa:
        return 0
    if stringa[0] in vocali:
        return 1+vowelCounter(stringa[1:])
    else:
        return 0+vowelCounter(stringa[1:])    

print(vowelCounter("Ciao"))