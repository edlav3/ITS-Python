'''Scrivi un programma per creare func1()una funzione che accetti argomenti di lunghezza variabile e ne stampi il valore.'''

from typing import Any

def func1(*args) -> list[Any]:
    print(*args)


lista=[]
quanti=int(input("Quanti elementi vuoi inserire?\n"))
for i in range(1,quanti+1):
    elemento=input(f"{i}° elemento: ")
    lista.append(elemento)
func1(*lista)