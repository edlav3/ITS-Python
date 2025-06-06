class ContactManager:
    def __init__(self, contatti:dict[str, list[str]]):
        self.contatti={}
    
    def create_contact(self, name:str, phone_numbers:list[str]):
        if name in self.contatti:
            raise NameError("Il contatto già esiste")
        else:
            self.contatti[name]=phone_numbers

    def add_phone_numbers(self, contact_name:str, phone_number:str):
        if contact_name not in self.contatti:
            return "Errore: il contatto non esiste"
        if phone_number in self.contatti[contact_name]:
            return "Errore: Il numero di telefono già eisste"
        self.contatti[contact_name].append(phone_number)
        return {contact_name: self.contatti[contact_name]}

    def remove_phone_number(self, contact_name:str, phone_number:str):
        if contact_name not in self.contatti:
            return "Errore: il contatto non esiste"
        if phone_number not in self.contatti[contact_name]:
            return "Errore: il numero di telefono non è presente"
        self.contatti[contact_name].remove(phone_number)
        return {contact_name:self.contatti[contact_name]}

    def update_phone_number(self, contact_name: str, old_phone_number:str, new_phone_number:str):
        if contact_name not in self.contatti:
            return "Errore: il contatto non esiste"
        if old_phone_number not in self.contatti[contact_name]:
            return "Errore: il numero di telefono non è presente"
        self.contatti[contact_name].remove(old_phone_number)
        self.contatti[contact_name].append(new_phone_number)
        return {contact_name: self.contatti[contact_name]}

    def list_contacts(self):
        lista=[]
        for key in self.contatti:
            lista.append(key)
        return lista

    def list_phone_numbers(self, contact_name:str): 
        if contact_name not in self.contatti:
            return "Errore: il contatto non esiste"
        return self.contatti[contact_name]

    def search_contact_by_phone(self, phone_number:str):
        tutti=[]
        for nomi, num in self.contatti.items():
            if phone_number in num:
                tutti.append(nomi)
        if len(tutti)!=0:
            return tutti
        else:
            return "Nessun contatto trovato con questo numero di telefono"