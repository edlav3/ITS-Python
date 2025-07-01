class Documento:

    def __init__(self):
        self.text=""
    
    def getText(self) -> str:
        return self.text
    
    def setText(self, text:str) -> None:
        self.text=text
    
    def isInText(self, parola:str) -> bool:
        verifica=False
        if parola in self.text:
            verifica=True
        return verifica
    

class Email(Documento):
    def __init__(self, text:str, mittente: str, destinatario:str, titolo:str):
        super().__init__()
        self.setText(text)
        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitolo(titolo)

    def setMittente(self, mittente: str) -> None:
        self.mittente=mittente
    
    def setDestinatario(self, destinatario: str) -> None:
        self.destinatario=destinatario
    
    def setTitolo(self, titolo: str) -> None:
        self.titolo=titolo
    
    def getMittente(self) -> str:
        return self.mittente
    
    def getDestinatario(self) -> str:
        return self.destinatario
    
    def getTitolo(self) -> str:
        return self.titolo
    
    def getText(self):
        super().getText()
        return (f"Da: {self.mittente}, A: {self.destinatario}\nTItolo: {self.titolo}\nMessaggio: {self.text}")
    
    def writeToFile(self, percorsoFile:str) -> None:
        with open(percorsoFile, "w") as file:
            file.write(self.getText())


class File(Documento):

    def __init__(self, text, nomePercorso: str):
        super().__init__()
        self.percorso=nomePercorso
        self.setText(text)

    def leggiTestoDaFile(self):
        with open(self.percorso, "r") as file:
            self.text=file.read()

    def getText(self):
        return f"Percorso: {self.percorso}\nContenuto: {self.text}"
    

testo="Ciao Mario, è un piacere risentirti"
mitt="andreafalcone2020@gmail.com"
dest="mariolazio1972@gmail.com"
titolo="Caro amico,"

mail=Email(testo, mitt, dest, titolo)
print(mail.getText())