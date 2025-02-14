lst=[]
for i in range(1,100001):
    lst.append(i)
print(lst)
minimo=min(lst)
massimo=max(lst)
print(f"La lista parte da {minimo} e fnisce a {massimo}")
somma=sum(lst)
print(f"La somma di tutti i numeri della lista è {somma}")