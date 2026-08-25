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


class Animal:
    def ladrar(self):
        raise NotImplementedError("Cada animal debe definir su forma de ladrar.")


class Perro(Animal):
    def ladrar(self):
        return "Guau, guau"


class Lobo(Animal):
    def ladrar(self):
        return "Auu, guau"


def mostrar_ladridos(animales):
    """Muestra el ladrido de cada animal usando el mismo metodo."""
    for animal in animales:
        print(f"{animal.__class__.__name__}: {animal.ladrar()}")


numero1 = 10
numero2 = 3

print(f"Suma: {numero1} + {numero2} = {sumar(numero1, numero2)}")
print(f"Resta: {numero1} - {numero2} = {restar(numero1, numero2)}")
print(f"Multiplicacion: {numero1} * {numero2} = {multiplicar(numero1, numero2)}")
print(f"Division: {numero1} / {numero2} = {dividir(numero1, numero2):.2f}")

print("\nEjemplo de polimorfismo:")
animales = [Perro(), Lobo()]
mostrar_ladridos(animales)
