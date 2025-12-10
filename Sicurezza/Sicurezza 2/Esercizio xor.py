stringa = input("Inserisci una stringa da cifrare: ")
key = int(input("Inserisci la chiave: "))
cifrati=[]
decifrati=[]
risultato=""
for i in stringa:
    cifrati.append(ord(i) ^ key)
print(f'Lista di caratteri cifrati: {cifrati}')

for i in cifrati:
    decifrati.append((i) ^ key)
print(f'Lista di caratteri decifrati: {decifrati}')

for i in decifrati:
    risultato+=chr(i)
print(f"La parola è: {risultato}")