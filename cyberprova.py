import requests
import hashlib

challenge = "http://challenge01.root-me.org/web-serveur/ch52/"
prova = "https://www.google.com" 
md5_hash = hashlib.md5(prova.encode()).hexdigest()
parametri = {
    'url': prova,
    'h': md5_hash
}
risposta=requests.get(challenge, params=parametri)
print(risposta.text)