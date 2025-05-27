'''Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate,
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.'''

def check_parentheses(expression: str) -> bool:
    verifica=False
    for i in expression:
        if i=="(":
            for i in expression:
                if i==")":
                    verifica=True
                else:
                    verifica=False
    return verifica

print(check_parentheses("()()"))
print(check_parentheses("(()))("))
print(check_parentheses(")("))
