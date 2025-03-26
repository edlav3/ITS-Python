'''Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
'''


def make_shirt(frase: str, taglia="L"):
    print(taglia)
    print(frase)


taglia=str(input("Che taglia è la maglietta? "))
frase=str(input("Quale frase vuoi stampata? "))

frasepredefinita="I love Python"

print("------------")
print("Maglietta 1")
make_shirt(frasepredefinita)

print("------------")
frasepredefinita="I love Python"
tagliapredefinita= "M"
print("Maglietta 2")
make_shirt(frasepredefinita, tagliapredefinita)

print("------------")
print("Maglietta 3")
make_shirt(taglia, frase)