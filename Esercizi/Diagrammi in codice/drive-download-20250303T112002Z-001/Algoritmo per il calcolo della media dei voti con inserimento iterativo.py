'''Progettare un algoritmo che consenta di inserire all'utente un elenco di voti non negativi relativi ad un esame, calcolandone la media.
L'algoritmo deve chiedere all'utente se vuole inserire un voto. 
Se la risposta è "SI", allora l'utente può procedere ad inserire il voto.
L'algoritmo deve consentire all'utente di inserire voti fin quando la risposta dell'utente sarà "NO". 
Infine, mostrare in output il valore medio dei voti inseriti.'''

quanti=0
media=0
somma=0
risposta=""
while True:
    risposta=input("Vuoi inserire un voto? Digita 'SI' o 'NO'")
    if risposta == "SI":
        voto=int(input("Voto: "))
        if voto>0:
            somma += voto
            quanti += 1
    if risposta=="NO":
        break
media=somma/quanti
print(f"Hai inserito {quanti} voti e la media è {media:.2f}")