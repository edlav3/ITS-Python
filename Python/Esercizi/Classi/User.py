'''Crea una classe chiamata User. Crea due attributi chiamati first_name e last_name,
quindi crea altri attributi che sono solitamente memorizzati in un profilo utente.
Crea un metodo chiamato describe_user() che stampa un riepilogo delle informazioni dell'utente.
Crea un altro metodo chiamato greet_user() che stampa un saluto personalizzato all'utente.
Crea diverse istanze che rappresentano utenti diversi e chiama entrambi i metodi per ogni utente.'''


class User:
    def __init__(self, first_name: str, last_name:str, age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def describe_user(self):
        print(f"Nome: {self.first_name}, cognome: {self.last_name}, anni: {self.age}")
    
    def greet_user(self):
        print(f"Benvenuto: {self.last_name} {self.first_name}")

utente1=User("Giacomino", "Bonaparte", 45)
utente2=User("Pino", "Silvestri", 32)
utente3=User("Diego", "Taddei", 22)

User.describe_user(utente1)
User.greet_user(utente1)
print("=============================")
User.describe_user(utente2)
User.greet_user(utente2)
print("=============================")
User.describe_user(utente3)
User.greet_user(utente3)