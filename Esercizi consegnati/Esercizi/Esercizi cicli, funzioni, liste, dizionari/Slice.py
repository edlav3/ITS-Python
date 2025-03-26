lst=[]
for i in range(1,100001):
    lst.append(i)
print(lst)
minimo=min(lst)
massimo=max(lst)
print(f"\nLa lista parte da {minimo} e fnisce a {massimo}")
somma=sum(lst)
print(f"La somma di tutti i numeri della lista è {somma}")

print("I primi elementi della lista sono:")
for i in range(3):
    print(lst[i])
print("Gli elementi centrali della lista sono:")
for i in range(49900, len(lst)):
    if i<49995 or i>50005:
        continue
    if i>49995 & i<50005:
        print(lst[i])


print("Gli ulimi eleemnti della lista sono:")
for i in range(99998, len(lst)+1):
    print(i)