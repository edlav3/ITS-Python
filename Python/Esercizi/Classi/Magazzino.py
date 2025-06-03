class Prodotto:
    def __init__(self, nome: str, quanti: int):
        self.nome = nome
        self.quanti = quanti

class Magazzino:
    def __init__(self):
        self.magaz = {}

    def aggiungi_prodotto(self, prodotto: Prodotto):
        if prodotto.nome in self.magaz:
            self.magaz[prodotto.nome]+=prodotto.quanti
        else:
            self.magaz[prodotto.nome]=prodotto

    def cerca_prodotto(self, nome: str) -> Prodotto:
        return self.magaz.get(nome, None)

    def verifica_disp(self, nome: str) -> str:
        prodotto = self.cerca_prodotto(nome)
        if prodotto:
            if prodotto.quanti > 0:
                return f"{nome} disponibile in quantità: {prodotto.quanti}"
            else:
                return f"{nome} non disponibile (quantità zero)"
        else:
            return f"{nome} non presente nel magazzino"



m = Magazzino()
p1 = Prodotto("Mouse", 10)
p2 = Prodotto("Tastiera", 0)

m.aggiungi_prodotto(p1)
m.aggiungi_prodotto(p2)

print(m.verifica_disp("Mouse"))       # Mouse disponibile in quantità: 10
print(m.verifica_disp("Tastiera"))    # Tastiera non disponibile (quantità zero)
print(m.verifica_disp("Monitor"))     # Monitor non presente nel magazzino