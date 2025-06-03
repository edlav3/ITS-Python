'''Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. Sia Pi una produttoria definita come segue:
Pi = (0 + 2) * (1 + 2) * (2 + 2) * ... * (n + 2).  

Calcolare il valore della produttoria Pi se n = 7.
'''

def produttoria(num) -> int:
    if num==0:
        return 2
    else:
        return (produttoria(num-1)*(num+2))

print(produttoria(7))