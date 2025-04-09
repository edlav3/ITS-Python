'''
Mentre programmeremo ci capiterà di dover rappresentare dati con degli standard,
ad esempio un cf deve avere 16 cifre, come possiamo fare per rapresentare gli standard?
Useremo le RegEx (Regular Expression), che sono un insieme di simboli che identificano in un testo un gruppo di stringhe,
danno possibilità di trovare un pattern in una stringa.

Le RegEx hanno una serie id elementi, le prima che  andremo a vedere sono le Ancore:
--- "^" -> Andremo a trovare le righe che iniziano con quella parola:
    Esempio: ^Ciao caro utente^

---  "$" -> Andremo a trovare le righe che finiscono con quella stringa:
    Esempio: $Addio carissimo$

--- "*" -> cerchiamo tutte le stringhe che hanno in comunei caratteri tranne alpiù l'ultimo carattere:
    Esempio: abc*, andrà a considerare "ab", "abc", "abcc", "abccccccc", etc

--- "+" -> cerchiamo tutte le stringhe che hanno in comune tutti i caratteri compreso almeno uno dell'ultimo:
    Esempio: abc+, considererà "abc", "abcccccc", ma non "ab"

--- "{n}" -> COnta quante volte compare una stringa:
    Esempio: abc{3}, considera "abccc" / a(bc){3}, considera "abcbcbc"

--- "{n,}" -> Almeno n volte:
    Esempio: abc{2}, considera "abcc", "abccc", "abcccc", etc

--- "{n, m}" -> Almeno tra n e m volte:
    Esempio: abc{2, 4}, considera "abcc", "abccc", "abcccc".

--- "." -> Ogni carattere in mezzo:
    Esempio: a.c, considera "abc", "afc", "a^c", non "abbbc" o "ac"

--- ".*" -> Tanta caratteri tra x e y:
    Esempio: a.*c, considera "ac", "acjnnfsvnc", etc

--- ".+" -> Tra x e y ci deve essere almeno un carattere:
    Esempio: a.+c, considera "afc", "assvfdcdcdsc", non "ac"

--- "|" -> Alternanza:
    Esempio: cane|gatto, considera "cane", "gatto" e "canegatto" o "gattocane"

--- "(...)" -> Cattura = permette di creare dei gruppi a cui possiamo fare sempre riferimento:
    Esempio: (abc)+, considera "abc", "abcabc" etc, non "abcabd"

--- "(?:...)" -> Gruppi che non catturano = non catturano il riferimento del testo:
    Esempio: (?:abcd)+, considera "ab", "cd", "abcd" etc

--- (?=...) -> Positive lookhead:
    Esempio: a(?=b), considera "a" solo se il carattere successivo è "b"

--- (?!...) -> Negative lookhead:
    Esempio: a(?!b), considera "a" solo se il carattere successivo non è "b"

'''