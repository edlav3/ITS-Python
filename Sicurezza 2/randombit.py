import sys #dove sys = system
import random

if len(sys.argv)!=2:
    print(f"Usage: {sys.argv[0]} <file name>")

#1) devo leggere tutti i file

with open(sys.argv[1], "rb") as f:
    data = f.read()  #read lo legge come stringa di byte

#2) devo scegliere un byte casuale del file
pos =random.randint(0, len(data)-1) # scrivo -1 perchè randint considera anche l'estremo superiore del file

#3) prendo un bit casuale del byte
bit=random.randint(0, 7)

#ora devo cambiare il valore del bit <bit> di data[pos] (uso xor)
#in sostanza devo costruire un byte di tutti 0 e un solo 1 nel posto giusto

byte=data[pos]
byte=byte ^ (1 << bit) # ho rovesciato il bit-esimo bit
# cambio solo il bit che mi interessa

#prendo il primo pezzo di stringa, aggiungo il byte, aggiungola restante parte di stringa
data=data[:pos] + bytes([byte]) + data[pos+1:]

with open(sys.argv[1], "wb") as f:
    f.write(data)

print(f"Modificato il bit {bit} al posto {pos} nel file {sys.argv[1]}")