nord_sud = int(input("Quante macchine vengono dalla direzione nord-sud?\n"))
est_ovest = int(input("Quante macchine vengono dalla direzione est-ovest?\n"))
soglia = 70
time_ns = 0
time_eo = 0
if (nord_sud > soglia and est_ovest > soglia):
    time_eo=50
    time_ns=50
elif nord_sud > soglia:
    time_ns=60
    time_eo=40
elif est_ovest > soglia:
    time_eo=60
    time_ns=40
else:
    time_ns = (nord_sud / (nord_sud+est_ovest)) * 100
    time_eo = (est_ovest / (est_ovest+nord_sud)) * 100
print(f"La spartizione del semaforo sarà la seguente:\n{time_ns:.2f}% per direzione nord-sud\n{time_eo:.2f}% per la direzione est-ovest\n")

    