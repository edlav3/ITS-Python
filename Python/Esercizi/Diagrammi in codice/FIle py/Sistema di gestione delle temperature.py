'''Sviluppare un algoritmo che chieda all'utente di inserire 7 temperature (una per ogni giorno della settimana). L'algoritmo deve:

calcolare la temperatura media,
controllare se tutte le temperature sono comprese tra 10 e 30:
Se sì, mostrare “Temperatura nella norma”.
verificare se almeno una temperatura è maggiore di 35 o minore di 5:
Se sì, mostrare “Allerta temperatura”.
Mostrare in output la media, il giorno della temperatura più alta e il giorno della temperatura più bassa espresso numericamente (es. 1 per lunedì, 2 per martedì, ecc.).'''



temp=10
i=1
norma=0
allerta=0
massimo=-100
minimo=100
giornomin=0
giornomax=0
somma=0
media=0
while i<=7:
    temp=int(input(f"Temperatura del {i}° giorno della settimana: "))
    if temp>=10 and temp<=30:
        norma+=1
        somma+=temp
        if temp>massimo:
            massimo=temp
            giornomax=i
        if temp<minimo:
            minimo=temp
            giornomin=i
    elif temp>=35 or temp<=5:
        allerta+=1
        somma+=temp
        if temp>massimo:
            massimo=temp
            giornomax=i
        if temp<minimo:
            minimo=temp
            giornomin=i
    i+=1
media=somma/7
if norma==7:
    print("Temperatura nella norma")
if allerta>=1:
    print("Allerta temperatura")

print(f"La media delle temperature è di {media:.1f} gradi;\nIl giorno più caldo è stato il {giornomax}° con {massimo} gradi;\nIl giorno più freddo è stato il {giornomin}° con {minimo} gradi;")