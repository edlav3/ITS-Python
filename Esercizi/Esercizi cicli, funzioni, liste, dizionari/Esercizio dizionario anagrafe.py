anagrafe_male={"Andrea":"Pierfranceschi", "Marco":"Gramendola", "Alessio":"Fantini"}
anagrafe_shemale={"Giulia":"Leo", "Federica":"Papaluca", "Alessia":"Marin"}

nomi_male=list(anagrafe_male.keys())
cognomi_male=list(anagrafe_male.values())
for i in range(len(nomi_male)):
    print(f"{nomi_male[i]} {cognomi_male[i]},")
    
nomi_shemale=list(anagrafe_shemale.keys())
cognomi_shemale=list(anagrafe_shemale.values())
for i in range(len(nomi_shemale)):
    print(f"{nomi_shemale[i]} {cognomi_shemale[i]},")