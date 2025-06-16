from datetime import *

x=datetime(2020, 5, 17)
y=datetime(2021, 4, 23)
impiegati={"mario": y, "pippo":date.today(), "mattia": x}
ultimo=max(impiegati.items())
print(ultimo)

ultima_assunzione=max(impiegati.items())
assunti={}
for impiegato, data in impiegati.items():
    assunti[data]=impiegato
print(assunti[ultima_assunzione])
