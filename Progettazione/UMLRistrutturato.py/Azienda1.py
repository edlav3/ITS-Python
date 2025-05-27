from enum import *
from typing import Any, Self
import re
from datetime import date

class CAP(str):
    def __new__(cls, cap:str|Self) -> Self:
        if re.fullmatch(r'\d{5}$'):
            return super().__new__(cls, cap)
        raise ValueError("Civico non valido")

class Indirizzo:
    _via:str
    _civico:str
    _cap: CAP
    def __init__(self, via:str, civ:str, cap: CAP):
        if not via or via.isdigit()==True:
            raise TypeError("La via non può essere vuota e non può contenere solo numeri")
        elif len(civ)>6:
            raise ValueError("Civico inesistente")
        self._via=via
        self._civico=civ
        self._cap=cap
    
    def via(self) -> str:
        return self._via
    
    def civico(self) -> str:
        return self._civico
    
    def cap(self) -> str:
        return self._cap


class PositiveInt(int): # la classe eredita dal tipo 'int'
    # tipo di dato intero > 0
    def __new__(cls, valore: int|float|str|bool|Self) -> Self:
        n:int = super().__new__(cls, valore)  # trasforma l'oggetto n in un oggetto int, super si riferisce alla superclasse di PositiveInt (ovvero int)
        if n>0:
            return n
        raise ValueError(f"Numero inseirto non positivo")


class Impiegato:
    _nome: str #noto alla nascita
    _cognome: str #noto alla nascita
    _nascita:date #<<immutabile>> e noto alla nascita
    _stipendio: PositiveInt


    def __init__(self, nome:str, cognome:str, nascita: date, stipendio: PositiveInt):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.nascita=nascita
        self.set_stipendio(stipendio)

    def nome(self) -> str:
        return self.nome
    
    def cognome(self) -> str:
        return self.cognome
    
    def nascita(self) -> str:
        return self.nascita
    
    def stipendio(self) -> float:
        return self.stipendio
    
    def set_nome(self, n:str) -> None:
        self._nome:str=n
    
    def set_cognome(self, c:str) -> None:
        self._nome:str=c

    def set_stipendio(self, s:str) -> None:
        self._nome:str=s


class Telefono: 
    def __init__(self):
        pass # da aggiungere


class Dipartimento: 
    _nome: str #noto alla nascita
    _telefoni:set[Telefono] # [1..*] noto alla nascita
    _indirizzo: Indirizzo|None #possibilmente non noto

    def __init__(self, nome:str, tel:Telefono, ind: Indirizzo|None) -> None:
        self.set_name(nome)
        self._telefoni=set() # creo l'insieme vuoto...
        self.add_telefono(tel) # ... poi invoco l'add
        self.set_indirizzo(ind)

    def nome(self) -> str:
        return self.nome
    
    def indirizzo(self) -> Indirizzo|None:
        return self.indirizzo
    
    def telefoni(Self) -> set[Telefono]:
        return set._telefoni
    
    def set_name(self, nome:str) -> None:
        self._nome:str = nome

    def set_indirizzo(self, ind: Indirizzo|None) -> None:
        self._indirizzo=ind
    
    def set_telefono(self, telefoni: set[Telefono]) -> None:
        if not telefoni: # equivalente a len(telefoni) >= 0, 
            raise ValueError("Il dipartimento deve avere almeno un numero id telefono")
        self._telefoni.add(telefoni)

    def add_telefono(self, telefoni: set[Telefono]) -> None:
        self._telefoni.add(telefoni)

    def remove_telefono(self, telefono: Telefono) -> None:
        if len(self._telefoni) >= 2:
            self._telefoni.remove(telefono)
        else:
            raise RuntimeError("Il dipartimento deve avere un numero di telefono")
    
