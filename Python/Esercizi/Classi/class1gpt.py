'''Esercizio: Creazione di una classe "Persona"

Crea una classe chiamata Persona che ha due attributi:

nome (una stringa)
età (un intero)
Aggiungi un metodo saluta che stampa un messaggio di saluto che include il nome della persona, ad esempio: "Ciao, mi chiamo Mario e ho 25 anni."

Aggiungi un altro metodo completa_anno che incrementa l'età della persona di 1 anno (come se fosse il suo compleanno)
e stampa un messaggio che dice che la persona ha compiuto un altro anno.

Crea un'istanza della classe Persona e prova i metodi.'''

class Persona:
    def __init__(self, nome:str, anni:int):
        self.nome = nome
        self.anni = anni

    def saluto(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.anni} anni")
    
    def completa_anno(self):
        self.anni+=1
        print(f"Auguri {self.nome}, dovrai spegnere {self.anni} candiline!")
    
persona1=Persona("Edoardo", 21)

persona1.saluto()
persona1.completa_anno()
persona1.saluto()    # nella stampa notiamo che il valore 21 è aumentato