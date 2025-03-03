'''Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario. Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"

Expected Output:

Digitare nome dell'utente: Mario Rossi
Digitare ruolo dell'utente: admin
Digitare l'età dell'utente: 30
Output: Accesso completo a tutte le funzionalità.

- - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Giulia Bianchi
Digitare ruolo dell'utente: utente
Digitare l'età dell'utente: 16
Output: Accesso limitato! Alcune funzionalità sono limitate!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Sara Neri
Digitare ruolo dell'utente: vip
Digitare l'età dell'utente: 22
Output: Attenzione! Ruolo non riconosciuto! Accesso Negato!

 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Luca Verdi
Digitare ruolo dell'utente: moderatore
Digitare l'età dell'utente: 25
Output: Salve Luca Verdi! Può gestire i contenuti ma non modificare le impostazioni.'''



persona={}
nome=str(input("Digitare nome dell'utente: "))
ruolo=str(input("Digitare ruolo dell'utente: "))
anni=int(input("Digitare età dell'utente: "))

persona['Nome']=nome
persona['Ruolo']=ruolo
persona['Anni']=anni

match (persona['Ruolo'], persona['Anni']):
    case ("Admin", _):
        print("Accesso completo a tutte le funzionalità")
    case ("Moderatore", _):
        print(f"Salve {nome}! Può gestire i contenuti ma non modificare le impostazioni.")
    case ("Utente", anni) if anni>=18:
        print("Accesso standard a tutti i servizi")
    case ("Utente", anni) if anni<=18:
        print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case ("Ospite", _):
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")
