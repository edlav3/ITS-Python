'''Problema 2: 10 punti, facoltativo
Premessa: nell'RSA, per calcolare con python l'esponente privato nota la chave pubblica e noti i due numeri primi p e q, si utilizza la sequente funzione
d = inverse(e, phi) dove ph = (p-1)*(q-1).

Sia dato n (pari a p*q) = 51151902024533551
e siano
e (esponente pubblico) = 3
C=10002041662569686 il messaggio cifrato (l'originale è una parola di sette caratteri alfanumerici)
Decifrare il messaggio
NB: un attacco forza bruta su 7 caratteri ha un costo computazionale pari a 62^6 = 56.800.235.584 (infattibile in python)
NB: ma n=p*q e quindi se riuscissi a trovare i due numeri primi che fattorizzano n, allora potrei applicare euclide inverso (la funzione inverse) per trovare la chiave privata...'''


from Crypto.Util.number import inverse

# Dati
n = 51151902024533551
e = 3
C = 10002041662569686

def fattorizza(n):
    fattori=[]
    div=2 # inizio dal primo numero primo
    while div*div<=n: # fintanto che div^2 non è maggiore di n
        while n%div==0: # fintanto che n è divisibile per div
            fattori.append(div) #aggiungi div
            n=n//div # dividi per div e aggiorna n
        div+=1 # incrementa divisore
    if n>1:  # Se n è ancora maggiore di 1, n è un numero primo (=> non ho trovato divisori)
        fattori.append(n)
    return fattori


fattori = fattorizza(n)
p, q=fattori[0], fattori[1]
print("p =", p, "q =", q)

phi=(p-1)*(q-1)
print(phi)

e=inverse(e, phi) # funzione inversa
decifrato=pow(C, e, n) # C^e % n

bytes_decifrato=decifrato.to_bytes(decifrato.bit_length(), 'big') # converto il numero decifrato in una sequenza di byte
                                                                # big, prende prima i bit più significativi, che hanno più peso
stringa_decifrata=bytes_decifrato.decode("utf-8") # decodifico in formato UTF-8

print(stringa_decifrata)