'''Il valore di π può essere approssimato utilizzando la seguente serie infinita:

π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari per ottenere approssimazioni sempre più accurate.
Quindi:

progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.
Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.'''


def cambio_segno(obiettivo="3.14"):
    pi = 4
    segno = -1
    denominatore = 1
    conteggio=1
    pigreco = 4
    while True:
        denominatore+=2
        pigreco+=(pi/denominatore)*segno
        segno*=-1
        conteggio+=1
        if str(pigreco)[:len(obiettivo)]==obiettivo:
            print(f"{obiettivo} si ottiene dopo {conteggio} iterazioni")
            break

cambio_segno(obiettivo="3.14")
cambio_segno(obiettivo="3.141")
cambio_segno(obiettivo="3.1415")
cambio_segno(obiettivo="3.14159")