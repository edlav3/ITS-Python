'''Creare una classe LotteriaMacchina contiene un elenco contenente una serie di 10 numeri e 5 lettere.
Implementare un metodo per selezionare casualmente 4 elementi (numbers o letters) da questo elenco per estrarre un biglietto vincente.
Infine, implementa un metodo per visualizzare un messaggio che dice che qualsiasi biglietto corrispondente ai 4 oggetti vincenti vince un premio.'''

import random

class LotteryMachine:
    def __init__(self):
        self.lista=[str(i) for i in range(1,11)] + ['A', 'B', 'C', 'D', 'E']
        self.vincente=[]

    def estrazione(self):
        self.vincente=random.sample(self.lista, 4)   #random.sample() si usa per selezionare 4 elementi casuali dall'elenco di numeri e lettere e assegnarli a vincente
        print(f"E' stato estratto il biglietto numero {self.vincente}")
    
    def verifica(self, biglietto):
        if sorted(biglietto)==sorted(self.vincente):
            print("Congratulazioni hai vinto")
        else:
            print("Spiacente, non è il biglietto vincente")

lotteria=LotteryMachine()

lotteria.estrazione()

biglieto_prova=["A", "4", "1", "Q", "H"]

lotteria.verifica(biglieto_prova)