from formagenerica import Formagenerica
#importo la classe

class Rettangolo(Formagenerica): # la classe rettangolo è sottoclasse di Formagenerica
    def __init__(self):
        super().__init__()
        self.setshape("rettangolo")

    def draw(self) -> None:
        