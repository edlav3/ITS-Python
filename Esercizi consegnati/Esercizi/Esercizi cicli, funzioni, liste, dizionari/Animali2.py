'''crea diversi dizionari, dove ogni dizionario rappresenta un animale domestico diverso.
In ogni dizionario, includi il tipo di animale e il nome del proprietario.
Memorizza questi dizionari in un elenco chiamato animali domestici. Quindi, fai un ciclo nell'elenco e, mentre
lo fai, stampa tutto ciò che sai su ogni animale domestico. '''


animale1={"Animale": "Conisglio", "Proprietario": "Mirko Lasagna"}
animale2={"Animale": "Criceto", "Proprietario": "Massimo Pericolo"}

animali_domestici=(animale1, animale2)
for item in animali_domestici:
    print(f"Animale: {item['Animale']}, Proprietario: {item['Proprietario']}\n")