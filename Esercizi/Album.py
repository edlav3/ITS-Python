def make_album(artist_name:str, title_album:str, canzoni=None) -> dict:
    disco={
        "Artista":artist_name,
        "Titolo album":title_album,
        "Numero canzoni": canzoni
    }
    return disco

nome1=input("Cantante preferito?")
album1=input("Quale album ti piace di più?")
nome2=input("Secondo cantante preferito?")
album2=input("Quale album ti piace di più?")
nome3=input("Terzo cantante preferito?")
album3=input("Quale album ti piace di più?")
num=input("Quante canzoni ha l'album?\n")
artista1=make_album(nome1, album1)
artista2=make_album(nome2, album2)
artista3=make_album(nome3, album3, num)
print(f"\n{artista1},\n{artista2},\n{artista3}")
