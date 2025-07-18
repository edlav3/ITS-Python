from random import *

def genera(dim: int) -> list[list]:
    matrice=[]
    for x in range(dim):
            riga=[]
            primo=randint(0,13)
            riga.append(primo)
            while len(riga)<dim:
                 num=randint(0,13)
                 if num!=primo:
                      riga.append(num)
            matrice.append(riga)
    return matrice


def printMAT(matrice:list[list]) -> None:
    for riga in matrice:
        for num in riga:
            print(f"{num:5}", end="")
        print()


def calcolaCarico(matrice: list[list], r:int, c:int) -> int:
    sommaRiga=sum(matrice[r])
    sommaColonne=0
    for riga in matrice:
        sommaColonne+=riga[c]
    carico=sommaRiga-sommaColonne
    return carico
    

def caricoNullo(matrice):
    zeri=[]
    for x in range(len(matrice)):
         for y in range(len(matrice)):
            eccolo=calcolaCarico(matrice, x, y)
            if eccolo==0:
                coppia=(x, y)
                zeri.append(coppia)
    if not zeri:
        zeri.append("Nessuno")
    print(f"   Indici per cui k=0: {zeri}")


matrice=genera(10)
printMAT(matrice)
print(f"   k(3,1): {calcolaCarico(matrice, 2, 0)}")
caricoNullo(matrice)