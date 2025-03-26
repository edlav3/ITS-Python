'''crea un dizionario chiamato luoghi_preferiti. Pensa a tre nomi da usare come chiavi nel dizionario e
memorizza da uno a tre luoghi preferiti per ogni persona. Per rendere questo esercizio un po' più interessante,
chiedi ad alcuni amici di nominare alcuni dei loro luoghi preferiti. Scorri il dizionario e stampa il nome di ogni persona
e i suoi luoghi preferiti.'''


luoghi_preferiti={"Pippo": "Sanremo", "Luis Sal": "Bologna", "Matteo Picarazzi": "Roma"}
for nome, luogo in luoghi_preferiti.items():
    print(f"A {nome} piace {luogo}")