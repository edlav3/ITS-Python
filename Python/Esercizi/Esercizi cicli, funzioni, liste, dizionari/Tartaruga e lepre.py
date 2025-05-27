import random


def tartaruga(pTartaruga:int):
    num=random.randint(1, 10)
    if 1<=num<=5:
        pTartaruga+=3
    elif 6<=num<=8:
        pTartaruga+=1
    else:
        pTartaruga-=6
        if pTartaruga<0:
            pTartaruga=1
    return pTartaruga
    
    
def lepre(pLepre:int):
    num=random.randint(1, 10)
    if num==1 or num==2:
        pLepre=pLepre
    elif num==3 or num==4:
        pLepre+=9
    elif num==5:
        pLepre-=12
        if pLepre<0:
            pLepre=1
    elif 5<=num<=7:
        pLepre+=1
    elif 9<=num<=10:
        pLepre-=2
        if pLepre<0:
            pLepre=1
    return pLepre


def posizioni(casella_tartaruga, casella_lepre):
    caselle=[]
    vuota="_"
    for index in range(1, 71):
        caselle.append(vuota)
    i=0
    while True:
        casella_lepre=lepre(casella_lepre)
        casella_tartaruga=tartaruga(casella_tartaruga)
        if casella_lepre<70:
            caselle[i]=="L"
        else:
            print("Ha vinto la lepre")
            break
        if casella_tartaruga<70:
            caselle[i]=="T"
        else:
            print("Ha vinto la tartaruga")
            break
        if casella_tartaruga==casella_lepre:
            caselle[i]=="OUCH!"
        print(*caselle)
        i+=1


print("'BANG !!!!! AND THEY'RE OFF !!!!!'")
posizioni(0,0)