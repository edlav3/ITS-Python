lst=[]
i=0
while i<100000:
    i+=1 
    lst.append(i)
print(lst)
minimo=min(lst)
massimo=max(lst)
print(f"\nLa lista parte da {minimo} e fnisce a {massimo}")
somma=sum(lst)
print(f"La somma di tutti i numeri della lista è {somma}")

print("I primi elementi della lista sono:")
a=0
while a<3:
    a+=1
    print(lst[a])
print("Gli elementi centrali della lista sono:")
b=49994
while b<len(lst):
    b+=1
    if b<49995 or b>50005:
        continue
    if b>49995 & b<50005:
        print(lst[b])

print("Gli ulimi eleemnti della lista sono:")
c=99995
while c<100000:
    c+=1
    print(c)