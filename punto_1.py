"""
RETO 1: PUNTO 1
Crear una función que realice operaciones básicas (suma, resta, multiplicación,
división) entre dos números,según la elección del usuario, la forma de entrada
de la función será los dos operandos y el caracter usado para la operación.
"""

def suma(a: int, b: int) -> int:
    return a + b
def resta(a: int, b: int) -> int:
    return a - b
def multiplicacion(a: int, b: int) -> int:
    return a * b
def division(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def main():
    operacion=str(input())
    a = int(operacion.split()[0])
    b = int(operacion.split()[1])
    c = operacion.split()[2]
    if c == "+":
        print(suma(a,b))
    elif c == "-":
        print(resta(a,b))
    elif c == "*":
        print(multiplicacion(a,b))
    elif c == "/":
        print(division(a,b))

if __name__ == "__main__":
    main()