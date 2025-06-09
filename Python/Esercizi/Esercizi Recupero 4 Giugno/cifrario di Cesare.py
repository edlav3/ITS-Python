from string import ascii_lowercase, ascii_uppercase

lettere=ascii_lowercase
lettere2=ascii_uppercase

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
        elif s[i] in lettere2:
            indiceAlfabeto=lettere2.index(s[i])
            posizione=indiceAlfabeto+key
            if posizione>=26:
                posizione%=26
            carattere=lettere2[posizione]
            lista+=carattere
        else:
            lista+=s[i]
        i+=1
    return lista


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
        elif s[i] in lettere2:
            indiceAlfabeto=lettere2.index(s[i])
            posizione=indiceAlfabeto-key
            if posizione>=26:
                posizione%=26
            carattere=lettere2[posizione]
            lista+=carattere
        else:
            lista+=" "
        i+=1

    return lista

prova="hello world!AA!!Aa"
ancoraprova=caesar_cypher_encrypt(prova, 13)
print(ancoraprova)
print(caesar_cypher_decrypt(ancoraprova, 13))