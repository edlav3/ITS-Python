'''Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente.'''


massimo=float('-inf')
i=1
while i<=4:
    num=float(input(f"{i}° numero: "))
    if num>massimo:
        massimo=num
    i+=1
print(f"Trai 4 numeri, {massimo} è il più grande")