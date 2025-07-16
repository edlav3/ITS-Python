from datetime import datetime
from typing import Self
from enum import *


class RealGEZ(float):
    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        n: float = super().__new__(cls, v)
        if n >= 0:
            return n
        raise ValueError(f"Il numero inserito {v} è negativo!")


class IntGEZ(int):
    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        n: int = super().__new__(cls, v)
        if n >= 0:
            return n
        raise ValueError(f"Il numero inserito {v} è negativo!")


class Utente:
    _username: str #<<imm>> {id}
    _registrazione: datetime #<<imm>>

    def __init__(self, registrazione: str, username:datetime):
        self._registrazione=registrazione
        self._username=username

    def get_reg(self) -> datetime:
        return self._registrazione
    
    def get_us(self) -> str:
        return self._username
    
    def __hash__(self) -> int:
        return hash((self._username))
    
    def __eq__(self, other: Self) -> bool:
        if hash(self)!=hash(other):
            return False
        return self._username == other._username


class Privato(Utente):
    def __init__(self, registrazione, username):
        super().__init__(registrazione, username)


class Bid:
    _istante: datetime #<<imm>> {id}
    _asta_bid:dict['Asta', 'AstaBid']

    def __init__(self):
        self._istante=datetime.now()
    
    def get_istante(self) -> datetime:
        return self._istante
    
    def add_link_coinvolto(self, l:'AstaBid._link'):
        if l._bid not in self._asta_bid:
            self._asta_bid[l._bid()]=l
        else:
            raise ValueError("Link già presente")

    def remove_link(self, l: 'AstaBid._link'):
        if l._bid() is not self:
            raise ValueError("Fermo!")
        if l._bid() in self._asta_bid:
            self._asta_bid.pop(l._bid())
        else:
            raise ValueError("Il link non esiste")


class Condizione(StrEnum):
    da_sistemare=auto()
    discreto=auto()
    buono=auto()
    ottimo=auto()


class PostOggetto:
    _prezzo:RealGEZ
    _anniG:IntGEZ
    _descrizione:str
    _pubblicaz:datetime #<<imm>>
    _is_nuovo:bool #<<imm>>
    _condizione:Condizione #solo se usato

    def __init__(self, prezzo:RealGEZ, anniG:IntGEZ, descrizione:str, pubblicaz:datetime, is_nuovo:bool, condizione:Condizione):
        if self._is_nuovo==True:
            raise ValueError ("Un oggetto nuovo non ha condizione")
        elif self._is_nuovo==None:
            raise ValueError ("Non è stato specificato se l'oggetto è nuovo o usato")
        else:
            self.set_condizione(condizione)
        self._pubblicaz=pubblicaz
        self._is_nuovo=is_nuovo
        self.set_prezzo(prezzo)
        self.set_anniG(anniG)
        self.set_descrizione(descrizione)

    def set_prezzo(self, prezzo:RealGEZ):
        self._prezzo=prezzo
    def set_anniG(self, anniG:IntGEZ):
        self._anniG=anniG
    def set_descrizione(self, descrizione:str):
        self._descrizione=descrizione
    def set_condizione(self, condizione:str):
        self._condizione=condizione
        
    def prezzo(self) -> RealGEZ:
        return self._prezzo
    def anniG(self) -> datetime:
        return self._anniG
    def descrizione(self) -> str:
        return self._descrizione
    def condizione(self) -> Condizione:
        return self._condizione


class Asta(PostOggetto):
    _prezzoBid: RealGEZ
    _scadenza: datetime
    _asta_bid:dict[Bid, 'AstaBid']

    def __init__(self, prezzo: RealGEZ, anniG: IntGEZ, descrizione: str, pubblicaz: datetime, is_nuovo: bool,
                 condizione: Condizione, prezzoBid: RealGEZ, scadenza: datetime):
        super().__init__(prezzo, anniG, descrizione, pubblicaz, is_nuovo, condizione)
        if scadenza<self._pubblicaz:
            raise ValueError("La scadenza non può essere precedente alla pubblicazione del post")
        self.set_prezzoBid(prezzoBid)
        self.set_scadenza(scadenza)

    def set_prezzoBid(self, prezzo: RealGEZ) -> None:
        self._prezzoBid=prezzo
    def set_scadenza(self, scadenza: datetime) -> None:
        if scadenza<self._pubblicaz:
            raise ValueError("La scadenza non può essere precedente alla pubblicazione")
        self._scadenza=scadenza

    def scadenza(self) -> datetime:
        return self._scadenza

    def prezzoBid(self) -> RealGEZ:
        return self._prezzoBid

    def add_link_AstaBid(self, l: 'AstaBid._link'):
        if l._asta not in self._asta_bid:
            self._asta_bid[l._asta()]=l
        else:
            raise ValueError("Link già presente")

    def remove_link(self, l: 'AstaBid._link'):
        if l._asta() is not self:
            raise ValueError("Fermo!")
        if l._asta() in self._asta_bid:
            self._asta_bid.pop(l._asta())
        else:
            raise ValueError("Il link non esiste")
        

class AstaBid:
    #classe factory
    @classmethod
    def add(cls, asta: Asta, bid: Bid) -> None:
        # crea il link (impiegato, bid)
        l = cls._link(asta, bid)
        asta.add_link_AstaBid(l)
        bid.add_link_AstaBid(l)
        asta.remove_link(l)
        bid.remove_link(l)
    
    class _link:
        # ogni oggetto di questa class rappresenta un link di associazione AstaBid
        # ovvero una coppia (Impiegato, bid)
        _asta: Asta
        _bid: Bid
        def __init__(self, asta: Asta, bid: Bid):
            self._asta=asta
            self._bid=bid

        def impiegato(self):
            return self._asta

        def bid(self):
            return self._bid