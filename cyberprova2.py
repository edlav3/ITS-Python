import requests

challenge = "http://challenge01.root-me.org/web-serveur/ch2/"

parametri = {
    'User-Agent': 'admin'
}
risposta=requests.get(challenge, headers=parametri)
print(risposta.text)