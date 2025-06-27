import math

def calculateCharges(ore: float) -> int:
    tariffa=0
    ore=math.ceil(ore)
    if ore<0:
        pass
    elif ore<=3:
        tariffa=2
    elif ore<24:
        tariffa= 2+(ore-3)*0.50
    elif ore==24:
        tariffa=10
    else: 
        pass
    return tariffa

ancora=input("Inserire una macchina? (si / no): ")
clienti=[]
while ancora!="no":
    cliente=[]
    ore=float(input("Ore che si desidera parcheggiare: "))
    if ore>24:
        print("Parcheggio sopra le 24 ore non consentito")
    elif ore<0:
        print("Ore non valide")
    else:
        tariffa=calculateCharges(ore)
        cliente.append(ore)
        cliente.append(tariffa)
        clienti.append(cliente)
    ancora=input("Inserire una macchina? (si / no): ")

print("\n")

for i in range(len(clienti)):
    if i==0:
        print(f"{'Cliente':<12}{'Ore':<10}{'Tariffa':<10}")
    print(f"{i+1:<12}{clienti[i][0]:<10}{clienti[i][1]:<10}")
    if i==len(clienti)-1:
        print(f"{'Totale':<12}{sum([cliente[0] for cliente in clienti]):<10}{sum([cliente[1] for cliente in clienti]):<10}")
