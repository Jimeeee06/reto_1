"""
RETO 1: PUNTO 4
Escribir una función que reciba una lista de números enteros y retorne la mayor
suma entre dos elementos consecutivos.
"""
def max_suma(numeros: list) -> int:
    sumas = []
    #itera sobre la lista de números y suma cada par de elementos consecutivos
    for i in range(0, len(numeros)-1):
        suma = int(numeros[i]) + int(numeros[i+1])
        sumas.append(suma)
    #retorna la suma máxima de la lista de sumas
    return(max(sumas))

def main():
    #convierte la lista de números en enteros
    numeros = list(input().split())
    print(max_suma(numeros))

if __name__ == "__main__":
    main()