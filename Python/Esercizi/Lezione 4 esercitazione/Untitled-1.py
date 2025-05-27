'''Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a
seconda del parametro to_fahrenheit. Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.'''


def convert_temperature(celsius:float, valore:True) -> float:
    celsius=(celsius*9/5) + 32
    if valore==False:
        celsius=0
    return celsius

temp=float(input("temperatura in gradi Celsius: "))
fahrenheit=convert_temperature(temp, True)
print(f"Temperatura in Fahrenheit: {fahrenheit:.1f}")