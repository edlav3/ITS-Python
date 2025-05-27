'''Crea una classe base chiamata Veicolo che ha i seguenti attributi:

marca (una stringa)
modello (una stringa)
anno (un intero che rappresenta l'anno di produzione)
La classe Veicolo deve avere:

Un metodo dettagli che stampa i dettagli del veicolo (marca, modello, anno).
Un metodo speciale __str__ che restituisce una stringa che descrive brevemente il veicolo (es. "Toyota Corolla, 2015").
Crea due classi derivate dalla classe Veicolo:

Auto, che aggiunge un attributo porte (numero di porte) e un metodo numero_di_porte che stampa quante porte ha l'auto.
Moto, che aggiunge un attributo cilindrata (cilindrata del motore) e un metodo info_moto che stampa la cilindrata della moto.
Testa il codice creando istanze di Auto e Moto, e invocando i metodi delle rispettive classi.'''

#Classe base Veicolo
class Veicolo:
    def __init__(self, marca:str, modello:str, anno:int):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def dettagli(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno di produzione: {self.anno}")
    
    def __str__(self):
        return f"{self.marca}, {self.modello}, {self.anno}"

#Classe derivata Auto
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, porte):
        super().__init__(marca, modello, anno)
        self.porte = porte
    
    def numero_porte(self):  # metodo
        print(f"L'auto ha {self.porte} porte\n")

#Classe derivata Moto
class Moto(Veicolo):
    def __init__(self, marca, modello, anno, cilindrata):
        super().__init__(marca, modello, anno)
        self.cilindrata = cilindrata
    
    def info_moto(self):  # metodo
        print(f"La moto ha una cilindrata di {self.cilindrata}cc.")

    
#creo le istanze:

auto1=Auto("Nissan", "Micra", 2008, 3)
moto1=Moto("Yamaha", "R1", 2019, 998)

print(auto1) # grazie al meotod str
auto1.dettagli()
auto1.numero_porte()

print(moto1)
moto1.dettagli()
moto1.info_moto()