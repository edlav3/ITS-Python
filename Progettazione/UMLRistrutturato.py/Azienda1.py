from enum import *
from typing import Any, Self
import re
from datetime import date
from collections import defaultdict

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
    
    def __str__(self) -> str:
        return f"{self._via}, {self._civico}, {self._cap}"


class PositiveInt(int): # la classe eredita dal tipo 'int'
    # tipo di dato intero > 0
    def __new__(cls, valore: int|float|str|bool|Self) -> Self:
        n:int = super().__new__(cls, valore)  # trasforma l'oggetto n in un oggetto int, super si riferisce alla superclasse di PositiveInt (ovvero int)
        if n>0:
            return n
        raise ValueError(f"Numero inserito non positivo")

class PositiveFloat(float): # la classe eredita dal tipo 'float'
    # tipo di dato float > 0
    def __new__(cls, valore: int|float|str|bool|Self) -> Self:
        n:float = super().__new__(cls, valore)  # trasforma l'oggetto n in un oggetto int, super si riferisce alla superclasse di PositiveInt (ovvero int)
        if n>0:
            return n
        raise ValueError(f"Numero inseirto non positivo")


class Telefono:
    def __init__(self, numero: str):
        if not re.fullmatch(r'\d{10}', numero):
            raise ValueError("Numero di telefono non valido")
        self._numero = numero

    def numero(self) -> str:
        return self._numero

    def __str__(self):
        return self._numero

    def __eq__(self, other):
        return isinstance(other, Telefono) and self._numero == other._numero

    def __hash__(self):
        return hash(self._numero)


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
        return self._nome
    
    def indirizzo(self) -> Indirizzo|None:
        return self._indirizzo
    
    def telefoni(Self) -> set[Telefono]:
        return set.telefoni
    
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

    

class Afferenza:
    _data_aff:date #<<immutabile>>
    def __init__(self, data_aff:date):
        self._data_aff=data_aff



class Impiegato:
    _nome: str #noto alla nascita
    _cognome: str #noto alla nascita
    _nascita:date #<<immutabile>> e noto alla nascita
    _stipendio: PositiveInt
    _progetti: dict['Progetto', 'Coinvolto']

    def __init__(self, nome:str, cognome:str, nascita: date, stipendio: PositiveInt):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_nascita(nascita)
        self.set_stipendio(stipendio)
        self._progetti={}

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> str:
        return self._nascita

    def stipendio(self) -> float:
        return self._stipendio

    def set_nome(self, n:str) -> None:
        self._nome:str=n

    def set_cognome(self, c:str) -> None:
        self._cognome:str=c

    def set_stipendio(self, s:PositiveInt) -> None:
        self._stipendio:PositiveInt=s

    def set_nascita(self, nascita: date) -> None:
        self._nascita=nascita

    def __str__(self) -> str:
        return f"{self._nome} {self._cognome} - Nascita: {self._nascita}, Stipendio: {self._stipendio}€"

    def add_link_coinvolto(self, l:'Coinvolto._link'):
        if l._progetto not in self._progetti:
            self._progetti[l.progetto()]=l
        else:
            raise ValueError("Link già presente")

    def remove_link(self, l: 'Coinvolto._link'):
        if l.impiegato() is not self:
            raise ValueError("Fermo!")
        if l.progetto() in self._progetti:
            self._progetti.pop(l.progetto())
        else:
            raise ValueError("Il link non esiste")


class Progetto:
    _nome:str
    _budget:PositiveFloat
    _impiegati:dict[Impiegato, 'Coinvolto']

    def __init__(self, nome:str, budget:PositiveFloat):
        self.set_nome(nome)
        self.set_budget(budget)
        self._impiegati={}

    def set_nome(self, nome:str) -> None:
        self._nome=nome
    
    def set_budget(self, budget:str) -> None:
        self._budget=budget

    def nome(self) -> str:
        return self._nome

    def budget(self) -> PositiveFloat:
        return self._budget

    def add_link_coinvolto(self, l: 'Coinvolto._link'):
        if l._impiegato not in self._impiegati:
            self._impiegati[l.impiegato()]=l
        else:
            raise ValueError("Link già presente")

    def remove_link(self, l: 'Coinvolto._link'):
        if l.progetto() is not self:
            raise ValueError("Fermo!")
        if l.impiegato() in self._impiegati:
            self._impiegati.pop(l.impiegato())
        else:
            raise ValueError("Il link non esiste")

    def is_coinvolto(self, impiegato: Impiegato) -> bool:
        return impiegato in self._impiegati
    
    def __str__(self) -> str:
        _impiegati_str = "\n".join([f"{impiegato} - {coinvolto}" for impiegato, coinvolto in self._impiegati.items()])
        return f"Progetto: {self._nome}, Budget: {self._budget}€\n\nImpiegati:\n{_impiegati_str}"
    

class Coinvolto:
    # questa è una classe factory: non ha oggetti suoi
    # serve solo a creare oggetti di un'altra classe (in questo caso, di classe Link)
    @classmethod
    def add(cls, impiegato: Impiegato, progetto: Progetto) -> None:
        # crea il link (impiegato, progetto)
        l = cls._link(impiegato, progetto)
        impiegato.add_link_coinvolto(l)
        progetto.add_link_coinvolto(l)
        impiegato.remove_link(l)
        progetto.remove_link(l)
    
    class _link:
        # ogni oggetto di questa class rappresenta un link di associazione Coinvolto
        # ovvero una coppi (Impiegato, Progetto)
        _impiegato: Impiegato
        _progetto: Progetto
        def __init__(self, impiegato: Impiegato, progetto: Progetto):
            self._impiegato=impiegato
            self._progetto=progetto

        def impiegato(self):
            return self._impiegato

        def progetto(self):
            return self._progetto


progetto = Progetto("Pegaso", PositiveInt(12.5))
imp1 = Impiegato("Mario", "Rossi", date(2023, 12, 12), 1)
imp2 = Impiegato("Pippo", "Franco", date(2010, 12, 23), 4)