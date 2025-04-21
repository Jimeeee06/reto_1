"""
RETO 1: PUNTO 3
Escribir una función que reciba una lista de números y devuelva solo aquellos
que son primos. La función debe recibir una lista de enteros y retornar solo
aquellos que sean primos.
"""
#verifica si un número es primo, si es menor o igual a 1 no es primo
#si es mayor a 1 verifica si es divisible por algún número entre 2 y
# la raíz cuadrada de n

import math

def primo(n: int) -> bool:
    if n <= 1:
        return False
    #verifica por cada número hasta la raíz cuadrada de n
    for i in range(2, int(math.sqrt(n)) + 1):
        #si n es divisible por alguno de ellos, no es primo
        if n % i == 0:
            return False
    return True

def main():
    #convierte la lista de números en enteros
    lista_inicial = list(map(int, input().split()))
    primos = []
    #verifica si cada número es primo, si lo es lo agrega a la lista de primos
    for n in lista_inicial:
        if primo(n):
            primos.append(n)
    print(primos)

if __name__ == "__main__":
    main()
