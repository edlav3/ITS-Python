'''Inizia con la classe dell'esercizio 9-1. Crea tre istanze diverse dalla classe e chiama describe_restaurant() per ogni istanza.'''


class Ristorante:
    def __init__(self, restaurant_name:str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nome ristorante: {self.restaurant_name}, tipo cucina: {self.cuisine_type}")

    def open_restauran(self):
        print(f"Il ristorante {self.restaurant_name} è aperto")
    

ristorante=Ristorante("Gianni al mattone", "Pizzeria")
ristorante2=Ristorante("MC donald", "Fast Food")
ristorante3=Ristorante("Instanbul Kebab", "Pizzeria/Kebab")
Ristorante.describe_restaurant(ristorante)
Ristorante.describe_restaurant(ristorante2)
Ristorante.describe_restaurant(ristorante3)