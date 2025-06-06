class Movie:
    def __init__(self, movie_id:str, title:str, director:str):
        self.movie_id=movie_id
        self.title=title
        self.director=director
        self.is_rented=False
    
    def rent(self):
        if self.is_rented==False:
            self.is_rented=True
        else:
            print (f"Errore: film {self.title} già noleggiato")
    
    def return_movie(self):
        if self.is_rented==False:
            print (f"Errore: film {self.title} già noleggiato")
        else:
            self.is_rented=False


class Customer:
    def __init__(self, customer_id:str, name:str):
        self.customer_id=customer_id
        self.name=name
        self.rented_movies=[]