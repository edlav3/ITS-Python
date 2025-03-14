alien_color=input("Quale alieno vuoi colpire? 'verde', 'giallo' o 'rosso'?")
if alien_color=="verde":
    print("Alieno colpito, hai guadgnato 5 punti!")
else:
    print("Alieno pericoloso mancato!")
while alien_color != "verde":
    alien_color=input("A quale alieno vuoi sparare ora?")
    if alien_color=="verde":
        print("Alieno colpito, hai guadgnato 5 punti!")
    else:
        print("Peccato, alieno mancato")