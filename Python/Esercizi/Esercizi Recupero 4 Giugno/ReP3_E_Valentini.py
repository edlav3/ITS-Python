from typing import Self
from random import randint

class PositiveInt(int):
    def __new__(cls, valore: int|float|str|bool|Self) -> Self:
        n:int = super().__new__(cls, valore) 
        if n>0:
            return n
        raise ValueError(f"Numero inserito non positivo")


class Creatura:
    __nome:str
    def __init__(self, nome:str):
        self.setNome(nome)

    def setNome(self, nome):
        if not nome or not isinstance(nome, str):
            self.__nome="Creatura generica"
        else:
            self.__nome=nome
    
    def nome(self) -> str:
        return self.__nome
    
    def __str__(self) -> str:
        return f"Creatura: {self.__nome}"


class Alieno(Creatura):
    __matricola:PositiveInt
    __munizioni:list[int]

    def __init__(self):
        self.__setMatricola()
        nome_alieno=f"Robot-{self.__matricola}"
        super().__init__(nome_alieno)
        self.__setMunizioni()

        if self.nome()!=f"Robot-{self.__matricola}":
            print("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")

    def __setMatricola(self) -> int:
        self.__matricola=randint(10000, 90000)
    
    def __setMunizioni(self) -> list[int]:
        self.__munizioni=[x**2 for x in range(15)]
    
    def matricola(self):
        return self.__matricola

    def munizioni(self):
        return self.__munizioni

    def __str__(self):
        return f"Alieno: {self.nome()}"


class Mostro(Creatura):
    __urlo_vittoria:str
    __gemito_sconfitta:str
    __assalto:list[int]

    def __init__(self, nome, urlo_vittoria:str, gemito_sconfitta:str):
        super().__init__(nome)
        self.__setAssalto()
        self.__setVittoria(urlo_vittoria)
        self.__setSconfitta(gemito_sconfitta)
        self.__assalto=[]

    def __setAssalto(self):
        self.__assalto=[randint(1, 100) for x in range(15)]

    def __setVittoria(self, vittoria:str):
        if vittoria and isinstance(vittoria, str):
            self.__urlo_vittoria=vittoria
        else:
            self.__urlo_vittoria="GRAAAHHH"
    
    def __setSconfitta(self, sconfitta:str):
        if sconfitta and isinstance(sconfitta, str):
            self.__gemito_sconfitta=sconfitta
        else:
            self.__gemito_sconfitta="Uuurghhh"
    
    def vittoria(self):
        return self.__urlo_vittoria
    
    def sconfitta(self):
        return self.__gemito_sconfitta
    
    def assalto(self):
        return self.__assalto
    
    def alternaLettere(self):
        risultato=""
        for x, y in enumerate(self.nome()):
            if x%2==0:
                risultato+=y.lower()
            else:
                risultato+=y.upper()
        return risultato

    def __str__(self):
        return f"Mostro: {self.alternaLettere()}"


def pariUguali(a:list[int], b:list[int]) -> list:
    c=[]
    for i in range(min(len(a), len(b))):
        if a[i]%2==0 and b[i]%2==0:
            c.append(1)
        else:
            c.append(0)
    return c


def combattimento(a:Alieno, m:Mostro):
    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("Errore, queste creature non esistono")
        return None
    count=0
    esito=pariUguali(a.munizioni(), m.assalto())
    for i in esito:
        if i==1:
            count+=1
    if count>=4:
        print(f"{m.vittoria()}\n"*3)
        return m
    else:
        print(m.sconfitta())
        return a


def proclamaVincitore(c):
    testo=str(c)
    w=len(testo) + 10
    l=5

    for i in range(l):
        if i==0 or i==l-1:
            print("*"*w)
        elif i==2:
            print("*", end="")
            print(testo, end="")
            print(" "*5, end="")
            print("*")
        else:
            print("*"+" "*(w-2)+"*")


m=Mostro("Godzilla", "GRAAAHH!", "Uuurghhh")
a=Alieno()

print(m)
print(a)

vincitore=combattimento(a, m)

if vincitore is not None:
    proclamaVincitore(vincitore)
