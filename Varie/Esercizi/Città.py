def describe_city(nome:str, paese: str): 
    print(f"Grazie, ora so che {nome} si trova in {paese}")

nome=input("Città preferita?")
paese=input("In quale paese si trova?")
describe_city(nome, paese)
