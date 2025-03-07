''' Scrivi un ciclo while che consenta agli utenti di immettere l'artista e il titolo di un album. Una volta ottenute queste informazioni,
chiama make_album() con l'input dell'utente e stampa il dizionario creato. Assicurati di includere un valore quit nel ciclo while.'''



def make_album(artist_name:str, title_album:str) -> dict:
    dati={
        "Artista":artist_name,
        "Titolo album":title_album,
    }
    return dati

lista=[]
esito=" "
while esito!="no":
    nome=input("Cantante preferito: ")
    album=input("Quale album ti piace di più?\n")
    artista=make_album(nome, album)
    lista.append(artista)

    esito=input("Vuoi aggiungere un altro artista? 'si' o 'no': ")
    if esito=="no":
        break

print("\n")
for i in range(len(lista)):
    print(*lista[i].values(), sep=', Album: ')