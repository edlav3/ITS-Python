def city_county(nome:str, paese: str): 
    print(f"{nome}, {paese}")

nome1=input("Città preferita?")
paese1=input("In quale paese si trova?")
nome2=input("Seconda città preferita?")
paese2=input("In quale paese si trova?")
nome3=input("terza città preferita?")
paese3=input("In quale paese si trova?\n")
city_county(nome1, paese1)
city_county(nome2, paese2)
city_county(nome3, paese3)