'''
Sia dato il messaggio decifro (convertito in numero intero in base 10): 

204751668535
Il messaggio decifro è stato ottenuto cifrando il messaggio originale con algoritmo RSA senza padding con n=514948966453 e esponente pubblico (e) pari a 3
Provare a decifrare il messaggio decifro
NB: il messaggio originale è una parola di cinque lettere maiuscole e minuscole.
NB: Quando il problema sembra arduo, allora un approccio brutale potrebbe essere quello vincente.'''

# assegnazione variabili 
cifrata = 204751668535
modulo = 514948966453
esponente = 3

continua = True
tentativi=0
lettere = "CySABDEFGHIJKLMNOPQRTUVWXYZabcdefghijklmnopqrstuvwxz"

for c1 in lettere: # primo carattere
    if continua == False:
        break
    for c2 in lettere: # secondo carattere
        for c3 in lettere: # terzo carattere
            for c4 in lettere: # quarto carattere
                for c5 in lettere: # quinto carattere
                    parola = c1 + c2 + c3 + c4 + c5 # componi la parola da confrontare
                    tentativi+=1
                    try:
                        testo = int(parola.encode("utf-8").hex(), 16)   # converto la parola in esadecimale e poi in formato leggibile con hex()
                        decifro = pow(testo, 3, modulo) # cifro la parola di prova...
                        if decifro == cifrata:  # verifico se la parola cifrata è uguale a quella iniziale
                            print(f"Trovato in {tentativi} tentativi\nLa parola è: {parola}") 
                            continua = False    # mi fermo
                    except:
                        continue