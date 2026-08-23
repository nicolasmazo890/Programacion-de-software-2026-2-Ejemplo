def sumar(numero1, numero2):
    """Suma dos numeros."""
    return numero1 + numero2


def restar(numero1, numero2):
    """Resta el segundo numero del primero."""
    return numero1 - numero2


def multiplicar(numero1, numero2):
    """Multiplica dos numeros."""
    return numero1 * numero2


def dividir(numero1, numero2):
    """Divide el primer numero entre el segundo."""
    if numero2 == 0:
        raise ValueError("No se puede dividir entre cero.")
    return numero1 / numero2


numero1 = 10
numero2 = 3

print(f"Suma: {numero1} + {numero2} = {sumar(numero1, numero2)}")
print(f"Resta: {numero1} - {numero2} = {restar(numero1, numero2)}")
print(f"Multiplicacion: {numero1} * {numero2} = {multiplicar(numero1, numero2)}")
print(f"Division: {numero1} / {numero2} = {dividir(numero1, numero2):.2f}")
