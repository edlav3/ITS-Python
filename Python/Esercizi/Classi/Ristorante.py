'''Restaurant: crea una classe chiamata Restaurant. Il metodo __init__() per Restaurant dovrebbe memorizzare due attributi:
restaurant_name e cuisine_type.
Crea un metodo chiamato describe_restaurant() che stampi queste due informazioni
e un metodo chiamato open_restaurant() che stampi un messaggio che indica che il ristorante è aperto.
Crea un'istanza chiamata restaurant dalla tua classe. Stampa i due attributi singolarmente e poi chiama entrambi i metodi.'''


class Ristorante:
    def __init__(self, restaurant_name:str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nome ristorante: {self.restaurant_name}, tipo cucina: {self.cuisine_type}")

    def open_restauran(self):
        print(f"Il ristorante {self.restaurant_name} è aperto")
    

ristorante=Ristorante("Gianni al mattone", "Pizzeria")
print(ristorante.restaurant_name)
print(ristorante.cuisine_type)
Ristorante.describe_restaurant(ristorante)
Ristorante.open_restauran(ristorante)