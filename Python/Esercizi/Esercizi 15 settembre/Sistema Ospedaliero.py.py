class Persona:
    _first_name: str
    _last_name: str
    _age:int
    def __init__(self, first_name: str, last_name: str):
        if isinstance(first_name, str) and isinstance(last_name, str):
            self._first_name=first_name
            self._last_name=last_name
            self._age=0
        elif not isinstance(first_name, str):
            self._first_name=None
            raise ValueError("Il nome deve essere una stringa")
        elif not isinstance(last_name, str):
            self._last_name=None
            raise ValueError("Il cognome deve essere una stringa")
        else:
            self._age=None
        
    def setName(self, first_name:str) -> None:
        if isinstance(first_name, str):
            self._first_name=first_name
        else:
            raise ValueError("Il nome inserito non è una stringa")
    
    def setLastName(self, last_name: str) -> None:
        if isinstance(last_name, str):
            self._last_name=last_name
        else:
            raise ValueError("Il cognome inserito non è una stringa")
    
    def setAge(self, anni: int) -> None:
        if isinstance(anni, int):
            self._age=anni
        else:
            raise ValueError("L'età deve essere un numero intero")
        
    def getName(self) -> str:
        return self._first_name
    
    def getLastName(self) -> str:
        return self._last_name
    
    def getAge(self) -> int:
        return self._age
    
    def greet(self) -> str:
        return f"Ciao, sono {self._first_name} {self._last_name}! Ho {self._age} anni"


class Dottore(Persona):
    _specialization:str
    _parcel:float
    def __init__(self, first_name:str, last_name:str, specialization:str, parcel: float):
        super().__init__(first_name, last_name)
        if isinstance(specialization, str):
            self._specialization=None
        else:
            raise ValueError("La specializzazione non è una stringa")
        
        if isinstance(parcel, float):
            self._parcel=None
        else:
            raise ValueError("La parcella non può essere un numero intero")
    
    def setSpecializzation(self, specializzation: str) -> None:
        if isinstance(specializzation, str):
            self._specialization=specializzation
        else:
            raise ValueError("La specializzazione deve essere una stringa")
        
    def setParcel(self, parcel: float) -> None:
        if isinstance(parcel, float):
            self._parcel=parcel
        else:
            raise ValueError("La parcella non può essere un numero intero")
    
    def getSpecializzation(self) -> str:
        return self._specialization
    
    def getParcel(self) -> float:
        return self._parcel
    
    def isAValidDoctor(self):
        if self._age>30:
            return f"Doctor {self._first_name} {self._last_name} is valid"
        else:
            return f"Doctor {self._first_name} {self._last_name} is not valid"

    def doctorGreet(self):
        self.greet()
        return f"Sono un medico {self._specialization}"


class Paziente(Persona):
    _idcode: str
    def __init__(self, first_name, last_name, idCode: str):
        super().__init__(first_name, last_name)
        self._idcode=idCode
    
    def setidCode(self, idCode:str) -> None:
        self._idCode=idCode
    
    def getidCode(self) -> str:
        return self._idCode
    
    def patientInfo(self) -> str:
        return f"{self._first_name} {self._last_name}\nID: {self._idCode}"

class Fattura:
    _lista: list[Paziente]
    _doctor: Dottore
    _fatture: int
    _salary: int
    def __init__(self, lista:list[Paziente], doctor: Dottore):
        if doctor.isAValidDoctor():
            self._lista=lista
            self._doctor=doctor
            self._fatture=len(lista)
            self._salary=0
        else:
            self._doctor=None
            self._fatture=None
            self._lista=None
            self._salary=None
            raise ValueError("Non è possibile creare la classe fattura poichè il dottore non è valido!")
        
    def getSalary(self) -> int:
        salary=self._doctor.getParcel() * len(self._lista)
        return salary
    
    def getFatture(self) -> float:
        self._fatture=len(self._lista)
        return self._fatture
    
    def addPatient(self, newPatient: Paziente) -> list:
        self._lista.append(newPatient)
        self.getSalary()
        self.getFatture()
        return f"Alla lista del Dottor {self._doctor.getLastName()} è stato aggiunto il paziente {newPatient.getidCode()}"
    
    def removePatient(idCode):
        pass