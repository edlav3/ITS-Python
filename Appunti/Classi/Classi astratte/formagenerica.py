'''
Immaginiamo di dover scrivere un metodo che disegni una forma geometrica.
Il problema è che non sappiamo che forma dover disegnare, un triangolo? un rettangolo?
Come possiamo fare per rendere universale il metodo?
Possiamo definire un metodo astratto: ovvero creiamo una classe, definiamo il metodo 
e lo dichiariamo come astratto, cioè che viene solo definito e che non ha corpo.
L'implementazione del metodo viene rimandata alle classi 'figlie'.

Come si renede astratta una classe?
'''

from abc import ABC, abstractclassmethod

class Formagenerica(ABC): # in questo modo dichiaro che la classe è astratta
    @abstractclassmethod # in questo modo definisco un metodo astratto
    def draw(self) -> None:
        pass

    def setshape(self, shape:int) -> None:
        if shape:
            self.shape=shape
        else:
            print("La stringa non può essere vuota")
    
    def getshape(self) -> str:
        return self.shape