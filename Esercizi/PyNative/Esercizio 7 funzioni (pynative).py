'''Di seguito è riportata la funzione display_student(name, age). Assegnale un nuovo nome show_tudent(name, age)e chiamala utilizzando il nuovo nome.

Dato :

def display_student(name, age):
    print(name, age)

display_student("Emma", 26)
Dovresti essere in grado di chiamare la stessa funzione usando

show_student(name, age)'''


def display_student(name, age):
    print(name, age)

display_student("Emma", 26)

def show_student(name, age):
    display_student(name, age)

show_student("Pino", 67)

