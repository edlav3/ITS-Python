'''L'ereditarietà ci permette di usare metodi e attributi di una classe
all'interno di una sottoclasse.
Esempio:
'''

class Animal: 
    def speak(self):
        print("Questo animale fa un suono")

class Dog(Animal):
    def abbaia(self):
        print("Bau")

cane=Dog()
cane.speak()
cane.abbaia()


'''Se capita che una suerclasse e una sottoclasse hanno due metodi con lo stesso nome,
succede che viene eseguito il metodo della sottoclasse. Questa caratteristica
è utile nel caso in cui vogliamo diversificare le operazioni di un metodo o se vogliamo
apliare le operazioni del metodo della sottoclasse, ad esempio se vogliamo fare operazioni aggiuntive con i nuovi dati della sottoclasse.

E' possibile craere attributi e metodi protetti in modo che, nel caso in cui il codice sia condiviso con qualcuno,
quei dati attributi o metodi che non devono essere modificati da altri.
Sono identificati da un "_" prima della dichiarazione, e sono da intendere come un "warning" per i programmatori.
esempio: _method()
'''

