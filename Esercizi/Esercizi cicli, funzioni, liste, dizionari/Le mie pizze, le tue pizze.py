menu=["margherita", "boscaiola", "crostino"]
for i in range(len(menu)):
    print(f"Mi piace la pizza {menu[i]}")
print("Mi piace molto la pizza!")

friend_pizzas=["margherita", "boscaiola", "napoli"]
nuova_pizza1="gamberetti"
menu.append(nuova_pizza1)
nuova_pizza2="tartufo"
friend_pizzas.append(nuova_pizza2)

print("\nLe mie pizze preferite sono:")
for i in range(len(menu)):
    print(f"{menu[i]}")
print("\nLe tue pizze preferite sono:")
for i in range(len(friend_pizzas)):
    print(f"{friend_pizzas[i]}")


