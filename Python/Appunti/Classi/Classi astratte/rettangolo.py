from formagenerica import Formagenerica
#importo la classe

class Rettangolo(Formagenerica): # la classe rettangolo è sottoclasse di Formagenerica
    def __init__(self):
        super().__init__()
        self.setshape("rettangolo")

    def draw(self) -> None:
        print(f"\n{self.getshape()}\n")

        for i in range(5):
            for j in range(10):
                #lato maggiore in alto del rettangolo
                if i==0 or i==4:
                    print("*", end=" ")
                
                #lati minori del rettangolo
                elif j==0 or j==9:
                    print("*", end=" ")
                
                # stampa spazi bianchi in mezzo
                else:
                    print(" ", end=" ")
            print("\n")