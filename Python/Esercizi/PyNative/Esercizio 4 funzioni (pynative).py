'''Scrivi un programma per creare una funzione show_employee()utilizzando le seguenti condizioni.

Dovrebbe accettare il nome e lo stipendio del dipendente e visualizzarli entrambi.
Se lo stipendio manca nella chiamata di funzione, assegnare il valore predefinito 9000 allo stipendio
'''

def show_employee(nome:str, stipendio=9000):
    print(f"Nome dipendente: {nome}")
    anno=stipendio*12
    print(f"Fatturato annuo: {anno}")


nome=input("Dipendente: ")
consenso=input("Vuoi dichiare quanto guadagni? 'si' o 'no': ")
if consenso=="si":
    stipendio=int(input("Stipendio: "))
    show_employee(nome, stipendio)
else:
    print("Va bene, per il calcolo verrà usato una cifra standard")
    show_employee(nome)
