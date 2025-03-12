'''Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente.'''


massimo=float('-inf')
i=1
while True:
    num=float(input(f"{i}° numero: "))
    if num>massimo:
        massimo=num
    i+=1
    if i==5:
        break
print(f"Il numero più grande è {massimo}")