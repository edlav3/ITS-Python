'''
Cosa succede se devo usare un'istanza di una classe dentro un'altra classe
'''

class Libro:
    def __init__(self):
        self.titolo = ""
        self.autore = ""
        self.genere:list[str] = []
    
    def set_titolo(self, titolo:str) -> None:
        self.titolo = titolo

    def set_autore(self, nome:str) -> None:
        self.autore = nome

    def set_genere(self, tipo_genere:list[str]) -> None:
        self.genere = tipo_genere

    def get_titolo(self) -> str:
        return self.titolo
    def get_autore(self) -> str:
        return self.autore
    def get_genere(self) -> list[str]:
        return self.genere


class Biblioteca:
    def __init__(self):
        self.libri:list[Libro] = []    # la classe Biblioteca ha liste di oggetti di tipo Libro
    
    def set_libro(self, libro:Libro) -> None:   # il metodo set_libro ha come argomento, oggetti di tip Libro
        self.libri.append(libro)
    
    def get_info(self) -> None:
        for libro in self.libri:
            print(f"Titolo: {libro.get_titolo()}, Autore: {libro.get_autore()}")


# codice driver

# creo libri

scaffale:Biblioteca = Biblioteca()

libro1:Libro= Libro()
libro1.set_titolo("Il fu Mattia Pascal")
libro1.set_autore("Luigi Pirandello")
libro1.set_genere(["Narrativa", "Romanzo"])

scaffale.set_libro(libro1)

libro2:Libro= Libro()
libro2.set_titolo("I sentieri dei nidi di ragno")
libro2.set_autore("Italo Calvino")
libro2.set_genere(["Avventura", "Romanzo"])

scaffale.set_libro(libro2)

scaffale.get_info()