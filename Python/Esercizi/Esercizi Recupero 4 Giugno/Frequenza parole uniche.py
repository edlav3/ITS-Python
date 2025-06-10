from string import ascii_lowercase

lettere=ascii_lowercase

def frequenza(stringa:str) -> dict[str:int]:
    dizionario={}
    corrente=""
    for s in stringa:
        if s.lower() in lettere:
            corrente+=s.lower()
        else:
            if corrente!="":
                if corrente in dizionario:
                    dizionario[corrente]+=1
                else:
                    dizionario[corrente]=1
            corrente=""

    if corrente in dizionario:
        dizionario[corrente]+=1
    else:
        dizionario[corrente]=1
    
    return dizionario

stringa="Ora che fai? Davvero non ti han detto che non sono il tipo, Da guardare a una festa, un pessimo partito? Son certo che nessuno te l'ha suggerito"
print(frequenza(stringa))