'''Progetta un algoritmo che forniti dall'utente 20 totali di vendita e i nomi dei venditori,
trova i due nomi dei venditori con il totale più alto e il totale più basso delle vendite.'''

massimo=float('-inf')
minimo=float('inf')
for i in range(5):
    nome=input(f"Nome {i+1}° venditore: ")
    vendita=float(input(f"Ha venduto in € un totale di: "))
    if vendita<minimo:
        minimo=vendita
        nomemin=nome
    if vendita>massimo:
        massimo=vendita
        nomemax=nome
print(f"La persona con la vendita più bassa è stata {nomemin} con {minimo:.2f}€")
print(f"La persona con la vendita più alta è stata {nomemax} con {massimo:.2f}€")