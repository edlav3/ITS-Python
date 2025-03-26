current_users=["Diablo444", "Acer11", "Amministratore", "Edaordo"]
new_users=["Diablo44", "Beatrice", "Amministratoe", "Acer12"]
i=0
for items in range(len(current_users)):
    if new_users[items] in current_users:
        print(f"'{new_users[items]}' già utilizzato")
        i+=1
if i==0:
        print("I nomi utenti sono tutti disponibili")
print(f"Gli utenti già utilizzati sono {i}")
