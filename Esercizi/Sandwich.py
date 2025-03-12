'''scrivi una funzione che accetti un elenco di elementi che una persona desidera in un sandwich.
La funzione dovrebbe avere un parametro che raccolga tutti gli elementi forniti dalla chiamata di funzione
e dovrebbe stampare un riepilogo del sandwich ordinato. Chiama la funzione tre volte, utilizzando ogni volta un numero diverso di argomenti.'''



def sandwich(*args):
    for i in args:
        print(*i, sep=', ')


elementi=[]
aggiungi=""
while aggiungi!="no":
    alimento=input("Alimento: ")
    elementi.append(alimento)
    aggiungi=input("Inseire un altro elemento? 'si' o 'no': ")

print("\nIl sandwich si compone di:")
sandwich(elementi)

lista=["madonna", "gesù", "padre Pio"]
sandwich(lista)
