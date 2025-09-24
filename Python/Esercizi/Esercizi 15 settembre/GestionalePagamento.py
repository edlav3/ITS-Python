class Pagamento:
    __importo: float

    def __init__(self):
        self.__importo=0.0
    
    def setImporto(self, importo: float) -> None:
        self.__importo=importo
    
    def getImporto(self) -> float:
        return self.__importo
    
    def dettagliPagamanento(self):
        return f"Importo del pagamento: {self.getImporto():.2f}€"


class PagamentoContanti(Pagamento):
    def __init__(self, importo):
        super().__init__()
        self.setImporto(importo)


    def dettagliPagamento(self):
        print(f"Pagamento in contanti, importo: {self.getImporto():.2f}€")


    def inPezziDa(self):
        pezzi=[500, 200, 100, 50, 20, 10, 5,
               2, 1, 0.50, 0.20, 0.10, 0.05,
               0.02, 0.01]
        importo=self.getImporto()
        resto=importo
        for pezzo in pezzi:
            if resto>=pezzo:
                count=resto//pezzo # numero intero di banconote/monete che servono
                resto=resto-(count * pezzo) # aggiorno l'importo residuo
                print(f"Sono necessari {count:.0f} pezzi da {pezzo:.2f}")


p1 = PagamentoContanti(1888.88)
p1.dettagliPagamento()  # Output: Pagamento in contanti - Importo: €1234.78
p1.inPezziDa()  # Output: quanti pezzi sono necessari per l'importo