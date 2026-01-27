import socket
import json

# Configurazione
HOST = "socket.cryptohack.org"
PORT = 11112

# Creiamo un socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # 1. Riceviamo il messaggio di benvenuto ("Welcome to...")
    # Leggiamo fino a 1024 byte
    initial_resp = s.recv(1024).decode()
    print(f"Server: {initial_resp.strip()}")

    # 2. Prepariamo e inviamo l'oggetto JSON richiesto
    # È fondamentale aggiungere il carattere \n alla fine!
    request = {"buy": "flag"}
    message = json.dumps(request) + "\n"
    s.sendall(message.encode())

    # 3. Riceviamo la risposta finale che contiene la flag
    final_resp = s.recv(1024).decode()
    print("Risposta con Flag:")
    print(final_resp)