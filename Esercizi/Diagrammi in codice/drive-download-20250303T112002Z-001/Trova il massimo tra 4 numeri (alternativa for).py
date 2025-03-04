'''Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente.'''


massimo=float('-inf')
for i in range(4):
    x=int(input(f"{i+1}esimo numero:"))
    if x>massimo:
        massimo=x
print(f"Il numero più grande dei numeri che hai inserito è {massimo}")