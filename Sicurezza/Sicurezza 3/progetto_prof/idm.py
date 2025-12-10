
alfalambda — 08/10/25, 18:50
lladdr 00:11:22:33:44:NN
Per mettere un macaddress differente per ogni client
Aprite in visual studio code il vostro file user<NN>.ovpn
Dopo la riga verb 3 aggiungere
lladdr 00:11:22:33:44:NN
alfalambda — 28/10/25, 15:06
sudo openvpn --config clients/user99.ovpn
alfalambda — 28/10/25, 16:38
sudo tcpdump -i any  -n -e
alfalambda — 28/10/25, 19:17
Tipo di allegato: acrobat
Lezioni Cybersecurity.pdf
1.46 MB
alfalambda — 11/11/25, 13:36
So che è una comunicazione su protocollo ETHERNET

42 b9 7f 47 b2 b3 mac destinazione
96 3f 82 94 7a 26 mac sorgente
08 00 indica il protocollo IP
Mostra
pacchetti.txt
8 KB
Completare la decodifica
alfalambda — 11/11/25, 13:46
per il prossimo lunedì
alfalambda — 17/11/25, 18:01
Tipo di allegato: acrobat
LEGGIMI.pdf
50.13 KB
# Struttura della cartella
server_flask.py
static/
    home.html
    errore.html
## Esempio di pagina home (static/home.html)
Mostra
LEGGIMI.md
4 KB
alfalambda — 18/11/25, 15:32
Immagine
alfalambda — 18/11/25, 17:39
Siete sulla stessa macchina su cui il server è in esecuzione (ip 127.0.0.1, porta 5000)
C’è un client che sta navigando (in questo caso siete voi stessi)
Possibili approcci
Uso il tool TCPDUMP
Uso il tool WireShark (e per casa lo provate e mi fate sapere come va sulla porta 127.0.0.1 in ambiente windows)
Scrivo un reverse proxy (un’applicazione che sta in ascolto su una porta, es. 4000, e per ogni richiesta che riceve la invia alla porta 5000 e viceversa) e stampo tutto quello che ricevo dai due lati
Oppure utilizzo APACHE HTTPD oppure NGINX o quant’altro in configurazione reverse proxy, attivando il log di tutto
Sapendo che i SOCKET (le librerie di comunicazione su internet) sono in una libreria dinamica, riscrivo in linguaggo C le due funzioni SEND e RECV e poi lancio il client (es: google-chrome) con la riga LD_LIBRARY_PATH=<la libreria con le mie due funzioni> google-chrome
Ogni volta che google-chrome farà SEND e RECV, sarà chiamata la mia libreria che stampa tutto e poi chiama la libreria originale
Scrivo un’estensione per google-chrome, la installo e la collego (hook) alla richiesta/ricezione delle pagine web. Per ogni comunicazione, la stampa
Uso l’applicazione SOCAT che fa esattamente da reverse proxy
Uso l’applicazione netcat oppure nc e la imposto come reverse proxy
alfalambda — 18/11/25, 19:02
```from flask import Flask, make_response, redirect, request
from pathlib import Path
from urllib.parse import unquote, urlparse, parse_qs

app = Flask(__name__)
STATIC_DIR = Path("static")
Mostra
message.txt
4 KB
alfalambda — 18/11/25, 19:20
from flask import Flask, make_response, redirect, request
from pathlib import Path
from urllib.parse import unquote, urlparse, parse_qs

app = Flask(__name__)
STATIC_DIR = Path("static")
Mostra
web.py
4 KB
alfalambda — 21/11/25, 16:58
openssl genrsa -out cakey.pem 4096
openssl req -new -x509 -days 3650 -key cakey.pem -out ca.crt -subj "/C=IT/ST=Lazio/L=Rome/O=ITS-SEC/CN=ITS CA"
alfalambda — 21/11/25, 17:07
openssl x509 –text –noout –in ca.crt
alfalambda — 21/11/25, 17:23
openssl genrsa -out my.key 2048
openssl req -new -key my.key -out my.csr
alfalambda — 21/11/25, 17:31
openssl req -text -noout -in my.csr
alfalambda — 21/11/25, 17:57
openssl x509 -req -in my.csr -out my.crt -days 365 -CA ca.crt -CAkey cakey.pem -set_serial 1
openssl x509 –text –noout –in my.crt
alfalambda — 21/11/25, 18:25
Tipo di allegato: acrobat
protocolli e certificati ecc-ok.pdf
2.45 MB
alfalambda — 21/11/25, 18:55
Tipo di allegato: acrobat
supporto.pdf
149.34 KB
alfalambda — 25/11/25, 12:26
docker run --rm -it --net host httpd:latest
docker run --rm -it -p 9000:80 httpd:latest
sudo netstat -anp --tcp | grep LISTEN
alfalambda — 25/11/25, 12:34
ip a | grep inet
docker exec -it 1d6b1aeaa910 /bin/bash -i
alfalambda — 25/11/25, 13:01
docker run --rm -it -p 9000:80 -v ./:/usr/local/apache2/htdocs  httpd:latest
udo netstat -anp --tcp | grep LISTEN
alfalambda — 25/11/25, 13:25
docker run --rm httpd:latest /bin/bash -i
docker run -it --rm httpd:latest /bin/bash -i
alfalambda — 25/11/25, 13:35
more httpd.conf
alfalambda — 25/11/25, 13:43
docker run -it --rm -v conf/:/pippo httpd:latest /bin/bash -i
docker run -it --rm -v ./conf/:/pippo httpd:latest /bin/bash -i
cp -a conf /pippo/
sudo chown -R its:its conf/
alfalambda — 27/11/25, 09:41
Tipo di allegato: archive
immagini.zip
123.68 KB
Tipo di allegato: archive
suoni.zip
1.38 MB
alfalambda — 27/11/25, 10:04
docker run -it --rm kalilinux/kali-last-release
https://hub.docker.com/r/kalilinux/kali-last-release
docker run -it --rm kalilinux/kali-last-release /bin/bash -i
[UNI21]KillAll96-Alessio — 27/11/25, 10:05
+
alfalambda — 27/11/25, 10:07
docker run -it --net host --name my-kali kalilinux/kali-last-release /bin/bash -i
docker start -ia my-kali
alfalambda — 27/11/25, 12:04
docker run --rm -it -p 9000:80 -v ./immagini/:/usr/local/apache2/htdocs  httpd:latest
docker run --rm -it -p 9000:80 httpd:latest
alfalambda — 27/11/25, 12:40
docker run --rm -it -p 9000:80 -v ./immagini/:/usr/local/apache2/htdocs httpd:latest
alfalambda — 27/11/25, 13:29
docker container commit my-kali my-kaly:01
alfalambda — 27/11/25, 13:38
docker run -it --net host --name my-kali --cap-add=NET_ADMIN --cap-add=NET_RAW my-kali:01  /bin/bash -i
nmap -A -T4 -Pn 10.70.1.146
alfalambda — 14:54
https://training.olicyber.it/challenges
DiamondKiller9 — 15:26
flag{sn4ck_sh3nan1gans}
flag{cookie_manipulation}
flag{IDOR_cookie}
flag{th3_sn4ck_1s_1n_th3_c00k13}
Groucho

 — 16:10
6+7à
alfalambda — 16:40
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import io
Mostra
flag01.py
4 KB
﻿
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import io
import re

# --- CONFIGURAZIONE ---
URL_PAGINA = "http://captcha.challs.olicyber.it/"
URL_POST = "http://captcha.challs.olicyber.it/next"
# Se sei su Windows, scommenta e indica il percorso di tesseract.exe:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def main():
    sessione = requests.Session() # Mantiene i cookie tra una richiesta e l'altra (fondamentale!)

    print(f"[*] Avvio sfida su: {URL_PAGINA}")
    response = sessione.get(URL_PAGINA)

    livello = 1
    
    while True:
        print(f"\n--- LIVELLO {livello} ---")
        
        if response.status_code != 200:
            print("Errore: Impossibile caricare la pagina.")
            break

        soup = BeautifulSoup(response.text, 'html.parser')

        # 1. TROVA L'IMMAGINE
        img_tag = soup.find('img')
        if not img_tag:
            print("Nessuna immagine trovata. Probabilmente la sfida è finita!")
            print("Contenuto finale:", soup.get_text()[:200]) # Stampa l'inizio del testo finale
            break

        img_url = img_tag.get('src')
        # Gestisce URL relativi
        img_url = urljoin(response.url, img_url)

        # 2. SCARICA E OCR
        try:
            img_resp = sessione.get(img_url)
            image = Image.open(io.BytesIO(img_resp.content))
            
            # Opzionale: visualizza l'immagine per debug (togli il commento se serve)
            # image.show() 

            # Configurazione per cercare solo cifre
            custom_config = r'--oem 3 --psm 6 outputbase digits'
            testo_estratto = pytesseract.image_to_string(image, config=custom_config)
            numero = "".join(filter(str.isdigit, testo_estratto))
            
            if not numero:
                print("OCR fallito: nessun numero trovato. Riprovo o termino.")
                break
                
            print(f"[*] Numero trovato: {numero}")

        except Exception as e:
            print(f"Errore durante l'elaborazione immagine: {e}")
            break

        # 3. TROVA L'URL PER LA POST (Dinamico)
        # Cerca un form per capire dove inviare i dati, se presente.
        form = soup.find('form')
        if form and form.get('action'):
            url_post = urljoin(response.url, form.get('action'))
        else:
            url_post = URL_POST

        # 4. INVIA LA SOLUZIONE
        # ATTENZIONE: Controlla il 'name' del campo input nel HTML. Spesso è 'solution', 'code', 'answer'.
        # Cerchiamo di indovinarlo prendendo il primo input type='text' o 'number' nel form
        nome_campo = 'soluzione' # Default
        if form:
            input_tag = form.find('input', {'type': ['text', 'number', 'text']})
            if not input_tag: 
                 # Fallback: a volte è un input hidden o senza type specificato
                 input_tag = form.find('input')
            
            if input_tag and input_tag.get('name'):
                nome_campo = input_tag.get('name')

        payload = {
            nome_campo: numero
        }

        print(f"[*] Invio {payload} a {url_post}")
        
        # La risposta della POST diventa la pagina per il prossimo ciclo
        response = sessione.post(url_post, data=payload)
        livello += 1

if __name__ == "__main__":
    main()
flag01.py
4 KB