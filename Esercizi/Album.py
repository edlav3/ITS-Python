def make_album(artist_name:str, title_album:str, canzoni="non pervenuto") -> dict:
    disco={
        "Artista":artist_name,
        "Titolo album":title_album,
        "Numero canzoni": canzoni
    }
    return disco

nome1=input("Cantante preferito: ")
album1=input("Quale album ti piace di più?\n")
nome2=input("Secondo cantante preferito: ")
album2=input("Quale album ti piace di più?\n")
nome3=input("Terzo cantante preferito: ")
album3=input("Quale album ti piace di più?\n" )
num=input("Quante canzoni ha l'album?\n")

artista1=make_album(nome1, album1, None)
artista2=make_album(nome2, album2, None)
artista3=make_album(nome3, album3, num)

print(*artista1.values(), sep=', ')
print(*artista2.values(), sep=', ')
print(*artista3.values(), sep=', ')