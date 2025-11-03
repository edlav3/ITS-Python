from scapy.all import sniff


# Funzione che viene chiamata ogni volta che arriva un pacchetto
def packet_callback(packet):
    print(packet.summary())  # Stampa un riepilogo del pacchetto
    # Se vuoi stampare il contenuto completo:
    # print(packet.show())


# Cattura pacchetti sulla rete
sniff(prn=packet_callback, count=10)  # count=10 cattura solo 10 pacchetti, rimuovi per infinito