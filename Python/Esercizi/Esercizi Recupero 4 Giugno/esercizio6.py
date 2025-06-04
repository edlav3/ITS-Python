'''Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45'''

lista1=[]
for i in range(1,15):
    if i%2==0:
        lista1.append(i)
nuova=", ".join(map(str, lista1))
print(f"a) {nuova}")


lista2=[]
for i in range(1,15, 3):
    lista2.append(i)
nuova=", ".join(map(str, lista2))
print(f"b) {nuova}")


lista3=[]
for i in range(30,-1, -5):
    lista3.append(i)
nuova=", ".join(map(str, lista3))
print(f"c) {nuova}")


lista4=[]
for i in range(5,46, 10):
    lista4.append(i)
nuova=", ".join(map(str, lista4))
print(f"d) {nuova}")

