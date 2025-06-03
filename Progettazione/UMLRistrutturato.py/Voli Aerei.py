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
        self.set_codice(codice)
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




class Compagnia:
    _nome:str   #noto alla nascita
    _anno:GreaterThan1900   #<<immutabile>> e noto alla nascita


    def __init__(self, nome:str, anno: GreaterThan1900):
        self.set_nome(nome)
        self.set_anno(anno)
   
    def nome(self) -> str:
        return self._nome
   
    def anno(self) -> int:
        return self._anno
   
    def set_nome(self, c:str) -> None:
        self._nome:str=c
   
    def set_anno(self, a:GreaterThan1900) -> None:
        self._anno=a



class Aeroporto:
    _nome:str   #noto alla nascita
    _codice:str     #noto alla nascita


    def __init__(self, nome:str, codice:str):
        controllo=bool(re.fullmatch(r"^[A-Z]{3}$", codice))
        if controllo==False:
            raise ValueError("Codice non corretto")
        self.codice=codice
        self._nome=nome



class Città:
    def __init__(self, nomeC, abitanti: PositiveNuetralInt):
        self.nomeC=nomeC
        self.abitanti=abitanti


    def __hash__(self) -> int:
        return hash((self.nomeC))
   
    def __eq__(self, other: Self) -> bool:
        if hash(self)!=hash(other):
            return False
        return self.nomeC == other.nomeC



class Nazione:
    def __init__(self, nomeN):
        self.nomeN=nomeN


    def __hash__(self) -> int:
        return hash((self.nomeN))
   
    def __eq__(self, other: Self) -> bool:
        if hash(self)!=hash(other):
            return False
        return self.nomeN == other.nomeN