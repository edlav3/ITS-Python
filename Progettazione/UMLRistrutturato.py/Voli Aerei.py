from typing import Any, Self
import re


class PositiveNuetralInt(int):
    # tipo di dato intero >= 0
    def __new__(cls, valore: int|float|str|bool|Self) -> Self:
        n:int = super().__new__(cls, valore)
        if n>=0:
            return n
        raise ValueError(f"Numero inserito non positivo")


class Volo:
    _codice:str     #<<immutabile>> e noto alla nascita
    _durata: PositiveNuetralInt     #noto alla nascita

    def __init__(self, codice, durata:PositiveNuetralInt):
        self._codice=codice
        self.set_durata(durata)
   
    def codice(self) -> str:
        return self._codice
   
    def durata(self) -> int:
        return self._durata
   
    def set_codice(self, c:str) -> None:
        self._codice:str=c
   
    def set_durata(self, d:PositiveNuetralInt) -> None:
        if d==0:
            raise ValueError("La durata del volo non può essere 0")
        self._durata=d




class GreaterThan1900(int):
    def __new__(cls, valore: int|float|str|bool|Self) -> Self:
        n:int = super().__new__(cls, valore)
        if n>1900:
            return n
        raise ValueError(f"Numero inserito non valido")



class Aeroporto:
    _nome:str   #noto alla nascita
    _codice:str     # <<immutabile>>, noto alla nascita


    def __init__(self, nome:str, codice:str):
        controllo=bool(re.fullmatch(r"^[A-Z]{3}$", codice))
        if controllo==False:
            raise ValueError("Codice non corretto")
        self._codice=codice
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, codice) -> str:
        self._codice=codice
    
    def codice(self) -> str:
        return self._codice


class Nazione:

    def __init__(self, nomeN):
        self.nomeN=nomeN

    def __hash__(self) -> int:
        return hash((self.nomeN))
   
    def __eq__(self, other: Self) -> bool:
        if hash(self)!=hash(other):
            return False
        return self.nomeN == other.nomeN

class Città:
    _nome=str
    _abitanti: PositiveNuetralInt
    _nazione:Nazione

    def __init__(self, nome, abitanti: PositiveNuetralInt):
        self.set_nome(nome)
        self.set_abitanti(abitanti)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome) -> None:
        self._nome=nome

    def abitanti(self) -> PositiveNuetralInt:
        return self._abitanti
    
    def set_abitanti(self, abitanti: PositiveNuetralInt) -> None:
        self._abitanti=abitanti
    
    def nazione(self) -> Nazione:
        return self._nazione
    
    def set_nazione(self, nazione:Nazione) -> None:
        try:
            self._nazione.remove_citta(self) # da imprementare metodo
        except AttributeError:
            pass
        nazione.add_citta(self) # da imprementare metodo

    def __hash__(self) -> int:
        return hash((self._nome))
   
    def __eq__(self, other: Self) -> bool:
        if hash(self)!=hash(other):
            return False
        return self._nome == other._nome



class Compagnia:
    _nome:str   #noto alla nascita
    _anno:GreaterThan1900   #<<immutabile>> e noto alla nascita
    _dir_comp_citt:Città # noto alla nascita, mutabile, da aggregazione


    def __init__(self, nome:str, anno: GreaterThan1900, citta: Città):
        self.set_nome(nome)
        self._anno=anno
        self.set_citta(citta)

    def nome(self) -> str:
        return self._nome
   
    def anno(self) -> int:
        return self._anno
    
    def citta(self):
        return self._dir_comp_citt
    
    def set_citta(self, citta: Città):
        self._dir_comp_citt=citta
   
    def set_nome(self, c:str) -> None:
        self._nome:str=c