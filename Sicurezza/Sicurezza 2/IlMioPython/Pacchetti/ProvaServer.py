from scapy.all import sniff

IFACE = "eth0"  # modifica con la tua interfaccia oppure metti None per default

def print_pkt(pkt):
    # stampa riepilogo compatto
    print(pkt.summary())
    # per vedere tutti i campi dettagliati, decommenta:
    # pkt.show()
    # per vedere gli esatti byte raw, decommenta:
    # print(bytes(pkt).hex())

if __name__ == "__main__":
    print(f"In ascolto su interface={IFACE} (CTRL-C per fermare)...")
    sniff(iface=IFACE, prn=print_pkt, store=0)