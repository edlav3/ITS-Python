def make_shirt(taglia: str, frase: str):
    print(taglia)
    print(frase)

taglia=str(input("Che taglia è la maglietta?"))
frase=str(input("Quale frase vuoi stampata?"))
print("------------")
print("Maglietta 1")
make_shirt(taglia, frase)
print("Maglietta 2")
make_shirt("S", "Me fai paura")