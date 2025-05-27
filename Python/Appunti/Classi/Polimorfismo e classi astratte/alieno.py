class Alieno:
    def __init__(self, pianeta:str):
        self.setpianeta(pianeta)
    
    def setpianeta(self, pianeta:str) -> None:
        if pianeta: # se pianeta == True, cioè non è vuoto
            self.pianeta=pianeta
        else:
            print("Errore, la stringa non può essere vuota")
    
    def getpianeta(self) -> str:
        return self.pianeta
    
    def speak(self) -> None:
        print("\nIo zono alieno")

    def __str__(self) -> str:
        return f"Alieno provieniente dal pianeta {self.getpianeta()}"