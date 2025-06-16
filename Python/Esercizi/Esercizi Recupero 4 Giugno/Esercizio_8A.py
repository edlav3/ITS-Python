'''Si Scriva in Python in un file frazioni.py una classe Frazione, i cui attributi privati siano rispettivamente n e denominatore.

Si definiscano i metodi __init__, setter, getter, __str__, value.
In particolare:
il metodo value(), deve restituire il valore della frazione, ovvero numeratore / denominatore arrotondato a 3 cifre decimali;
il metodo __str__ deve mostare in output la frazione nel seguente modo: "numeratore / denominatore ";
i metodi setter devono controllare che il valore inserito sia un intero,
in caso contrario il numeratore ed il denominatore devono essere impostati per default rispettivamente a 13 e 5.
Inoltre, il metodo setter relativo al denominatore deve assicurarsi che questo non sia mai uguale a 0. Nel caso in cui il denominatore passato sia 0,
impostarlo per default a 5.
Suggerimento: per verificare che il numeratore ed il denominatore siano numeri interi, usare la funzione is_integer().'''

class Frazione:
    _d: int
    _n: int
    def __init__(self, n, d):
        self.set_n(n)
        self.set_d(d)
    
    def set_d(self, d):
        if isinstance(d, int) or d!=0:
            self._d=d
        else:
            self._d=5
        return self._d
    
    def set_n(self, n):
        if isinstance(n, int):
            self._n=n
        else:
            self._n=13
        return self._n
    
    def get_d(self):
        return self._d

    def get_n(self):
        return self._n
    
    def value(self):
        return round((self._n/self._d), 3)
    
    def __str__(self):
        return f"{self._n} / {self._d}"