'''Crea una classe chiamata Prodotto che ha i seguenti attributi:

nome (una stringa)
prezzo (un numero decimale)
quantità (un intero che rappresenta la quantità disponibile nel magazzino)
La classe Prodotto deve avere:

Un metodo dettagli che stampa il nome, il prezzo e la quantità del prodotto.
Un metodo aggiorna_quantità che aggiorna la quantità disponibile del prodotto (ad esempio, per aggiungere o sottrarre la quantità quando un prodotto viene venduto o rifornito).
Un metodo speciale __str__ che restituisce una descrizione breve del prodotto (es. "Caffè, 2.50€, 100 unità").
Crea una classe chiamata Inventario che gestisce una lista di oggetti Prodotto. La classe Inventario deve avere:

Un attributo prodotti che è una lista di oggetti Prodotto.
Un metodo aggiungi_prodotto che aggiunge un prodotto all'inventario.
Un metodo rimuovi_prodotto che rimuove un prodotto dall'inventario per nome.
Un metodo statico visualizza_inventario che mostra tutti i prodotti presenti nell'inventario.
Testa il codice creando vari prodotti, aggiungendoli all'inventario, aggiornando le quantità e visualizzando l'inventario.'''



class Prodotto:
    def __init__(self, nome:str, prezzo:float, quanti:int):
        self.nome=nome
        self.prezzo=prezzo
        self.quanti=quanti
    
    def dettagli(self):
        print(f"Prodotto: {self.nome}, prezzo: {self.prezzo}, {self.quanti} unità")

    def aggiorna_quantita(self):
        self.quanti+=1
    
    def __str__(self):
        print(f"{self.nome}, {self.prezzo}, {self.quanti} unità")
    
class Inventario:
    def __init__(self, *prodotti, nome, prezzo, quanti):
        self.nome="pippo"    # ---------------------------------- RISOLVI DA QUA -----------------------------
    
    def aggiungi_prodotto(self):
        self.prodotti.append(Prodotto)
    
    def rimuovi_prodotto(self):
        self.prodotti.remove(self.nome)

    def visualizza(self):
        for i in range(len(self.prodotti)):
            print(self.prodotti[i])



prodotto=Prodotto("Carota", "0.30", 34)
Inventario.aggiungi_prodotto(prodotto)