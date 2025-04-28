from persona import Persona
from alieno import Alieno  # importiamo le classi dai file

# creo oggetto di tipo persona

pers:Persona= Persona('Mario', 'Draghi', 77)
print(pers)

superman:Alieno=Alieno("Krypto")
print(superman)

'''
Andando a controllare gli altri due file, ci accorgiamo che abbiamo scritto due metodi ("speak")
con nomi uguali ma che stampano due cose diverse.
In python esiste il concetto di polimorfismo: ci permette di definire un metodo con lo stesso nome
ma con comportamenti differenti.
'''

pers.speak()

superman.speak()

'''invoco metodi uguali ma che hanno comportamenti diversi'''