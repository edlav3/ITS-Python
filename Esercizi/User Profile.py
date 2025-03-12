'''Crea un profilo di te stesso chiamando build_profile(), usando il tuo nome e cognome e altre tre coppie chiave-valore che ti descrivono.
Tutti i valori devono essere passati alla funzione come parametri.
La funzione deve quindi restituire una stringa come "Eric Crow, età 45, capelli castani, peso 67"'''



def build_profile(nome, cognome, anni, luogonascita, patente):
    me={"Nome": nome, "Cognome": cognome, "Anni": anni, "Nato a": luogonascita, "Automunito":patente}
    return me


nome=input("Nome: ")
cognome=input("Cognome: ")
anni=int(input("Anni: "))
luogonascita=input("Nato a: ")
patente=input("Hai la patente: ")

persona = build_profile(nome, cognome, anni, luogonascita, patente)
print(f"{persona['Nome']} {persona['Cognome']}, anni {persona['Anni']}, nato a {persona['Nato a']}, automunito: {persona['Automunito']} ")