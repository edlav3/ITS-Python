''' scrivi una funzione che memorizzi informazioni su un'auto in un dizionario. La funzione dovrebbe sempre ricevere un produttore e un nome di modello.
Dovrebbe quindi accettare un numero arbitrario di argomenti di parole chiave.
Chiama la funzione con le informazioni richieste e altre due coppie nome-valore,
come un colore o una caratteristica opzionale. La tua funzione dovrebbe funzionare per una chiamata come questa:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Stampa il dizionario restituito per assicurarti che tutte le informazioni siano state memorizzate correttamente. '''


def make_car(nome, produttore, **args):
    auto={"Modello": nome, "Produttore": produttore, **args}
    return auto


nome=input("Nome modello: ")
produttore=input("Produttore: ")
dati={}
while True:
    altro=input("Vuoi aggiungere un altro dato? 'si' / 'no': ")
    if altro!="no":
        chiave=input("Nome della caratteristica che vuoi inserire: ")
        valore=input("Dato della caratteristica: ")
        dati[chiave]=valore
    else:
        break

auto=make_car(nome, produttore, **dati)
print("\n")
for chiave, valore in auto.items():
    print(chiave, valore, sep=': ')