x=int(input("Numeri:"))
lista=[]
for i in range(x+1):
    lista.append(i)
    if i==0:
        continue
    elif i==1:
        print("1st")
    elif i==2:
        print("2nd")
    elif i==3:
        print("3rd")
    else:
        print(f"{lista[i]}th")
