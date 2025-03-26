utenti=["admin", "Edoardo", "Mario", "Paolo", "Pippo"]
if len(utenti)==0:
    print("Lista utenti vuota")
for i in range(len(utenti)):
    if utenti[i]=="admin":
        print("Ciao admin, voi vedere un rapporto sullo stato?")
    else:
        print(f"Ciao {utenti[i]}, bentornato")