glossario={"reverse":"l'ordine di una lista diventa inverso", "range":"usata nei cicli for per iterare un numero n di volte", "tuzzu":"non significa niente", "while":"esegue una serie x di istruzioni fintanto che la condizione del while è verificata", "sort": "algoritmo di ordinamento in ordine crescente"}
chiavi=list(glossario.keys())
print(*chiavi)
valori=list(glossario.values())
print(*valori, "\n\n")

for i in range(len(chiavi)):
    print(chiavi[i])
    print(valori[i],"\n")