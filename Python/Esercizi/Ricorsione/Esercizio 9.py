'''Si scriva una funzione ricorsiva vowelRemover che elimini tutte le vocali da una stringa data e restituisca sotto forma di una nuova stringa la stringa originale ma senza le vocali.

Suggerimento: utilizzare l'operatore + per realizzare la concatenazione di stringhe al fine di costruire la stringa da restituire.'''


def vowelRemover(stringa:str) -> str:
    
    if stringa=="":
        return ""
    primo=stringa[0]
    vocali=('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    if primo not in vocali:
        return primo+vowelRemover(stringa[1:])
    else:
        return vowelRemover(stringa[1:])
    

print(vowelRemover("Ciao, mi chiamo Edoardo"))