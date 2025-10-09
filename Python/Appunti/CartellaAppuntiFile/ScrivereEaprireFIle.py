'''
Avere a che fare con i file in python è piuttosto semplice.
Un file dal punto di vista pratico è una sequenza di bit all'interno dell'hard disk, come come immagini, file mp3 ecc.
Andando a leggere i bit, il computer riesce a interpretarlo e a fornirci

Un file è diviso in tre parti principali:
- Header: sono ocntenute informazioni riguardo al nome, estensione, tipo, la dimensione (cosiddetti metadati);
- Corpo: file vero e proprio, dove la sequenza di bit trascrive il corpo del file
- End of file (EOF): un carattere speciale che fa capire al sistema operativo che ha raggiunto la fine del file.

PATH Assoluto: deriva dalla Root, è il percorso di un file partendo dalla cartella principale
Esempio: /home/its/ITS-Python/Esercizi/Classi/Esercizi vacanze Pasqua/Esercizio 1.py

PATH Relativo: introduciamo la Current working directory (CWD), è la cartella dove ci troviamo a lavorare in un dato momento;
Un path relativo è il percorso che separa la posizione del file che vogliamo utilizzare dalla CWD


Perchè è importante scrivere su file?
Ricordiamo che i programmi girano sulla memoria RAM, ciò significa che quello che scriviamo in un programma, se il computer si spegna,
perdiamo tutto quello che abbiamo scritto durante l'esecuzione.
I file servono per salvare i dati che abbiamo ottenuto eseguendo un programma. e ci permettono di riprendere il contenuto in un secondo momento.


vediamo in pratica come funzionano:

Funzione 'open': prende come parametro in input il PATH relativo di un file
è importante che il PATH sia relativo in quanto, altrimenti, il file potrà essere acceduto solo dal computer da cui è stato copiato il Path assoluto.
La funzione 'open' è built-in di python e ritorna un wraper. Un file che contiene risorse utili per il sistema.
'''

percorso: str= "Appunti/CartellaAppuntiFile/esempio.txt"
modalita: str= "r"
encoding: str= "utf-8"

file=open(percorso)  

output: str=file.read()
print(output)

'''
Se noi facciamo l'open di tanti file e non chiudiamo mai nessun file, il computer
dedica risorse al mantenimento di quel file. Se aprissimo molti file pesanti, il sistema operativo collasserebbe nel giro di qualche giorno.
Quindi --> le risorse una volta acquisite vanne rilasciate
'''

# per dire al sistema operativo di chiudere il file, occorre fare

file.close()

'''
se ci si dimentica di fare la chiusura del file, questo rimane 'dedicato' all'utente che ha aperto il file,
la risorsa non è più accessibile da nessun'altro
--> in alternativa posso fare:'''

with open('esempio.txt', 'w') as file:
    file.write("Ciao")

'''
con questo blocco with, deallochiamo in automatico risolrse che abbiamo usato, è una risorsa utile per non dimenticarci.
Se ci dimenticassimo di deallocare tanti file, occupiamo memoria --> sprechiamo risorse --> la mAcchina rallenta

'''



percorso: str= "Appunti/CartellaAppuntiFile/esempio.txt"
modalita: str= "w"
encoding: str= "utf-8"

file=open(percorso, modalita) # la variabile 'file' è un wrapper, un qualcosa che contiene qualcos'altro,
                              # contiene un'istanza della classe Text

output: str=file.write("Uova a temperatura ambiente 8, Zucchero 250 g, Farina 00 140 g, Fecola di patate 120 g, Baccello di vaniglia 1, Sale fino 1 pizzico, Per 850 g di crema pasticcera, Latte intero 500 g, Panna fresca liquida 125 g, Zucchero 175 g, Tuorli 5, Amido di mais (maizena) 55 g, Baccello di vaniglia 1, Per la crema chantilly, Panna fresca liquida 100 g")
print(output) # viene stampato il numero di caratteri del file


'''
Queste funzioni, write, open, read, vanno a richiamare delle funzioni del sistema operativo,
che mi permettono di entrare in contatto con l'hardware (file) della macchina
'''