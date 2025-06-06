from string import ascii_lowercase

lettere=ascii_lowercase

def caesar_cypher_encrypt(s:str, key:int) -> str:
    lista=""
    i=0
    while i < len(s):
        if s[i] in lettere:
            indiceAlfabeto=lettere.index(s[i])
            posizione=indiceAlfabeto+key
            if posizione>=26:
                posizione%=26
            carattere=lettere[posizione]
            lista+=carattere
        else:
            lista+=s[i]
        i+=1
    return lista

prova="ciao a tutti"
ancoraprova=caesar_cypher_encrypt(prova, 30)
print(ancoraprova)


def caesar_cypher_decrypt(s:str, key:int):
    lista=""
    i=0
    while i < len(s):
        if s[i] in lettere:
            indiceAlfabeto=lettere.index(s[i])
            posizione=indiceAlfabeto-key
            if posizione>=26:
                posizione%=26
            carattere=lettere[posizione]
            lista+=carattere
        else:
            lista+=" "
        i+=1
    
    return lista

print(caesar_cypher_decrypt(ancoraprova, 30))