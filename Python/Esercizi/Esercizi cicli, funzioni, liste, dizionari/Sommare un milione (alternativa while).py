lst=[]
i=0
while i<100000:
    i+=1
    lst.append(i)
print(lst)
minimo=min(lst)
massimo=max(lst)
print(f"La lista parte da {minimo} e fnisce a {massimo}")
somma=sum(lst)
print(f"La somma di tutti i numeri della lista è {somma}")