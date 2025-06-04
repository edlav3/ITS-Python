''' Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.'''


def funzione(lista:list[int]) -> dict:
    positivi=[]
    negativi=[]
    dizionario={}
    for i in lista:
        if i>=0:
            positivi.append(i)
            dizionario["Positivi"]=positivi
        else:
            negativi.append(i)
            dizionario["Negativi"]=negativi
        
    return dizionario

        
prova=(1, 34, 67, -87, 23, -89)
print(funzione(prova))