from typing import Self

class Film: 
    __id:int
    __title:str
    def __init__(self, id:int, title:str):
        self.__id=id
        self.__title=title
    
    def setId(self, id:int) -> None:
        self.__id=id
    
    def setTile(self, title:str) -> None:
        self.__title=title

    def getId(self) -> int:
        return self.__id
    
    def getTitle(self) -> str:
        return self.__title
    
    def isEqual(self, otherFilm:Self) -> bool:
        return self.getId()==otherFilm.getId()
    

class Azione(Film):
    __genere: str
    __penale:float
    def __init__(self, id, title, genere:str):
        super().__init__(id, title)
        self.__genere=genere
        self.__penale=3
    
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni:int):
        return self.__penale*giorni

class Commedia(Film):
    __genere: str
    __penale:float
    def __init__(self, id, title, genere:str):
        super().__init__(id, title)
        self.__genere=genere
        self.__penale=2.5
    
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni:int):
        return self.__penale*giorni


class Drama(Film):
    __genere: str
    __penale:float
    def __init__(self, id, title, genere:str):
        super().__init__(id, title)
        self.__genere=genere
        self.__penale=2
    
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni:int):
        return self.__penale*giorni


class Noleggio:
    _film_List: list[Film]
    _rented_film: dict[int: list[Film]]

    def __init__(self, film_list:list):
        self._film_List=film_list
        self._rented_film={}

    def isAvailable(self, film:Film) -> bool:
        for movie in self._film_List:
            if movie.getId() == film.getId():
                print("Il film scelto è disponibile")
                return True
            print("Il film scelto non è disponibile")
        return False
    
    def rentAMovie(self, film:Film, clientID:int):
        if self.isAvailable(film):
            self._film_List.remove(film)
            if clientID in self._rented_film:
                self._rented_film[clientID].append(film)
                print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
            else:
                self._rented_film[clientID]=[]
