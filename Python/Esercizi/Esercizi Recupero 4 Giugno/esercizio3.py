'''Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.'''

def funzione(prodotti: dict) -> dict:
    nuovo={}
    for key, value in prodotti.items():
        if value<=50:
            plus=round((value+((value*10)/100)), 2)
            nuovo[key]=plus
    return nuovo
    

listaProdotti={"Pane": 3.345, "Vino": 56, "Nutella": 5.99, "Monster Limited Edition": 5000}
print(funzione(listaProdotti))