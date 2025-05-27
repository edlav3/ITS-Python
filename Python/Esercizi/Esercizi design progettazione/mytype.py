'''Vediamo di fare qualche esercizio di prova. Ppt Design di
applicazioni in Python, slide 9'''

from enum import *  # libreria che serve per creare classi che rappresentano un insieme finito
from typing import Self  # importo il tipo speciale Self, ci servirà per scrivere annotazioni più chiare all'interno delle classi

class Genere(StrEnum): # La classe Genere eredita da StrEnum, oggetto della classe enum
    uomo=auto()  # auto fa parte della libreria enum
    donna=auto()

class Voto(int): # La classe Voto eredita dalla classe int, il voto è effettivamente un numero intero
    def __new__(cls, v: int|float|Self) -> Self: # creo uogetti di classe voto che avranno in input oggetti o di tipo int, o tipo float o di tipo Voto (Self, indica il tipo della classe)
        # metodo __new__ a differenza di __init__ crea un oggetto vuoto e ne restituisce un altro di qualche tipo
        if v < 18 or v > 30:
            raise ValueError("Il valore Voto deve essere compreso tra 18 e 30")
        return int.__new__(cls, v)

class Indirizzo:
    _via: str
    _civico: str # in questo modo dico che le variabili dovrebbero rimanere private
    def __init__(self, via:str, civico: str):
        self._via = via
        self._civico = civico
    
    def get_via(self) -> str:  # metodo che restituisce la via
        return self._via
    def get_civico(self) -> str:  # metodo che restituisce il civico
        return self._civico