def subtract(a:int, b:int):
    if a>b:
        differenza=a-b
    else:
        differenza=b-a

    return differenza



a=int(input("Primo numero: "))
b=int(input("Secondo numero: "))
differenza=subtract(a, b)
print(f"La differenza tra {a} e {b} è {differenza}")