'''Ti viene dato un numero intero N. Il tuo compito è stampare un rangoli alfabetico di dimensioni uguali a N
(Il rangoli è una forma di arte popolare indiana basata sulla creazione di motivi.)

Di seguito sono mostrate le diverse dimensioni dei rangoli dell'alfabeto:

#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----


#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

def trattinigiu(n):
    t="-"
    i=0
    while i<n:
        print(t*i)
        i+=1

def trattinisu(n):
    t="-"
    i=n
    while i>0:
        print(t*i)
        i-=1

def letteredx(*args):
    

lista=("a","b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "z")
n=int(input("Dammi un numero intero: "))
trattinisu(n)
trattinigiu(n)