'''Progetta un algoritmo che forniti dall'utente 20 totali di vendita e i nomi dei venditori,
trova i due nomi dei venditori con il totale più alto e il totale più basso delle vendite.'''

massimo=-99999999999
minimo=9999999999
dizionario={}
for i in range(5):
    nome=input(f"Nome {i+1}° venditore:")
    vendita=int(input(f"Ha venduto in € un totale di:"))
    dizionario[nome]=vendita
    if vendita<minimo:
        minimo=vendita
        nomemin=nome
    if vendita>massimo:
        massimo=vendita
        nomemax=nome
print(f"La persona con la vendita più bassa è stata {nomemin} con {minimo}€")
print(f"La persona con la vendita più alta è stata {nomemax} con {massimo}€")