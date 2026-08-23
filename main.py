def sumar(numero1, numero2):
    """Suma dos numeros."""
    return numero1 + numero2


def restar(numero1, numero2):
    """Resta el segundo numero del primero."""
    return numero1 - numero2


numero1 = 10
numero2 = 3

print(f"Suma: {numero1} + {numero2} = {sumar(numero1, numero2)}")
print(f"Resta: {numero1} - {numero2} = {restar(numero1, numero2)}")
