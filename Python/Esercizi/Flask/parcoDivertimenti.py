import json  # Libreria standard per gestire i JSON
from flask import Flask

# ---------------------------------------------------------
# 1. Definizione delle Classi (Senza libreria abc)
# ---------------------------------------------------------

class Ride:
    """
    Classe base. Simula una classe astratta lanciando errori
    se i metodi category() o base_wait() non vengono sovrascritti.
    """
    def __init__(self, ride_id, name, min_height_cm):
        self.id = ride_id
        self.name = name
        self.min_height_cm = min_height_cm

    def category(self):
        # Senza @abstractmethod, usiamo questo trucco:
        raise NotImplementedError("Devi implementare category() nella sottoclasse!")

    def base_wait(self):
        # Senza @abstractmethod, usiamo questo trucco:
        raise NotImplementedError("Devi implementare base_wait() nella sottoclasse!")

    def info(self):
        """Restituisce un dizionario con le informazioni base."""
        return {
            "id": self.id,
            "name": self.name,
            "min_height_cm": self.min_height_cm,
            "category": self.category(),
            "base_wait_min": self.base_wait()
        }

    def wait_time(self, crowd_factor=1.0):
        """Calcola l'attesa stimata."""
        # float() assicura che il fattore sia un numero decimale
        base = self.base_wait()
        stima = base * float(crowd_factor)
        return int(round(stima))


class RollerCoaster(Ride):
    def __init__(self, ride_id, name, min_height_cm, inversions):
        # Chiamata al costruttore della classe padre
        super().__init__(ride_id, name, min_height_cm)
        self.inversions = inversions

    def category(self):
        return "roller_coaster"

    def base_wait(self):
        return 40

    def info(self):
        # Prendo il dizionario base e aggiungo il campo specifico
        data = super().info()
        data["inversions"] = self.inversions
        return data


class Carousel(Ride):
    def __init__(self, ride_id, name, min_height_cm, animals):
        super().__init__(ride_id, name, min_height_cm)
        self.animals = animals

    def category(self):
        return "family"

    def base_wait(self):
        return 10

    def info(self):
        data = super().info()
        data["animals"] = self.animals
        return data


class Park:
    def __init__(self):
        self.rides = {}

    def add(self, ride):
        self.rides[ride.id] = ride

    def get(self, ride_id):
        # Restituisce l'oggetto o None se non esiste
        if ride_id in self.rides:
            return self.rides[ride_id]
        return None

    def list_all(self):
        # Restituisce una lista dei soli valori (gli oggetti Ride)
        return list(self.rides.values())


# ---------------------------------------------------------
# 2. Configurazione Parco e Dati
# ---------------------------------------------------------

park = Park()

# Creazione delle istanze
rc1 = RollerCoaster("rc1", "Vortex", 140, 5)
car1 = Carousel("car1", "Magic Kingdom", 0, ["cavallo", "cigno", "tigre"])
rc2 = RollerCoaster("rc2", "Speed Demon", 120, 2)

# Aggiunta al parco
park.add(rc1)
park.add(car1)
park.add(rc2)


# ---------------------------------------------------------
# 3. Applicazione Flask
# ---------------------------------------------------------

app = Flask(__name__)

def crea_risposta_json(dati):
    """
    Funzione helper per restituire un JSON valido senza usare jsonify.
    Restituisce: (stringa_json, status_code, headers)
    """
    json_str = json.dumps(dati)
    headers = {'Content-Type': 'application/json'}
    return json_str, 200, headers

@app.route("/")
def home():
    # Creiamo i link manualmente come stringhe
    response_data = {
        "service": "Welcome to Park API",
        "description": "System for managing theme park rides.",
        "links": [
            "/rides",
            "/rides/rc1",
            "/rides/rc1/wait/1.5"
        ]
    }
    return crea_risposta_json(response_data)


@app.route("/rides")
def get_all_rides():
    rides_list = park.list_all()
    
    # Creiamo una lista di dizionari
    results = []
    for ride in rides_list:
        results.append(ride.info())
        
    return crea_risposta_json(results)


@app.route("/rides/<ride_id>")
def get_ride_detail(ride_id):
    ride = park.get(ride_id)
    
    if ride is not None:
        return crea_risposta_json(ride.info())
    else:
        # Gestione manuale dell'errore 404
        error_msg = {"error": "Ride not found"}
        return json.dumps(error_msg), 404, {'Content-Type': 'application/json'}


@app.route("/rides/<ride_id>/wait/<crowd>")
def get_ride_wait(ride_id, crowd):
    ride = park.get(ride_id)
    
    if ride is None:
        return json.dumps({"error": "Ride not found"}), 404, {'Content-Type': 'application/json'}
    
    # Conversione manuale del parametro crowd
    try:
        crowd_val = float(crowd)
    except ValueError:
        return json.dumps({"error": "Il fattore crowd deve essere un numero"}), 400, {'Content-Type': 'application/json'}

    estimated_time = ride.wait_time(crowd_val)
    
    response_data = {
        "ride": ride.name,
        "crowd_factor": crowd_val,
        "estimated_wait_minutes": estimated_time
    }
    
    return crea_risposta_json(response_data)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)