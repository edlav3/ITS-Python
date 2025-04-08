'''Scrivere una funzione ricorsiva recursiveDigitCounter che restituisca il numero di cifre di un numero intero n passato in input.
Sono permessi sia valori positivi che negativi per n.
Ad esempio, il numero -120 ha 3 cifre.
Non si tenga conto di eventuali zeri non significativi.

Suggerimento: per il calcolo delle cifre, fare un controllo se il valore assoluto di n sia minore di 10. In caso positivo,
significa che il numero n ha una sola cifra. In caso negativo, significa che il numero n ha più cifre;
dunque, dividere n per 10 per rimuovere l'ultima cifra e richiama ricorsivamente la funzione, fino a ottenere un numero con una sola cifra.'''


def recursiveDigitCounter(num:int):
    num=str(num)
    if not num:
        return 0
    if num[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        return 1+recursiveDigitCounter(num[1:])
    else:
        return 0+recursiveDigitCounter(num[1:])

print(recursiveDigitCounter(-12345678))