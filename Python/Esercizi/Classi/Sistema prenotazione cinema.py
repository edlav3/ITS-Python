class Film: 
    def __init__(self, titolo: str, durataMin: int):
        self.titolo=titolo
        self.durata=durataMin

class Sala:
    def __init__(self, numeroSala: int, film: Film, postiTot: int, postiOcc: int):
        self.numeroSala=numeroSala
        self.film=film
        self.postiTotali=postiTot
        self.postiOccupati=postiOcc
    
    def prenota_posti(self, prenotazione: int) -> str:
        if self.postiOccupati>=self.postiTotali:
            return "Errore, posti disponibili insufficienti"
        else:
            self.postiOccupati+=prenotazione
            return "Prenotazione effettuata, stai per essere indirizzato al pagamento"
    
    def posti_disponibili(self):
        return self.postiTotali-self.postiOccupati
    

class Cinema:
    def __init__(self):
        self.sale=[]

    def aggiungi_sala(self, sala:Sala):
        self.sale.append(sala)

    def prenota_film(self, titolo:str, posti: int):
        for sala in self.sale:
            if sala.posti_disponibili() >= posti:
                return sala.prenota_posti(posti)
            else:
                return "Posti insufficienti per questo film."
        return "Film non trovato in nessuna sala."


film1 = Film("Inception", 148)
sala1 = Sala(1, film1, 100, 0)

cinema = Cinema()
cinema.aggiungi_sala(sala1)

print(cinema.prenota_film("Inception", 5))  #prenotazione effettuata
print(cinema.prenota_film("Inception", 200))  #posti insufficienti
print(cinema.prenota_film("Avatar", 1))  #film non trovato