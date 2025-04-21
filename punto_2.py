"""
RETO 1: PUNTO 2
Realice una función que permita validar si una palabra es un palíndromo.
Condición: No se vale hacer slicing para invertir la palabra y verificar que
sea igual a la original.
"""

#se comparan los caracteres desde los extremos hacia el centro, si no es igual
# se retorna False, si todos son iguales se retorna True

def palindromo(word: str) -> bool:
    length = len(word)
    #Compara los caracteres desde los extremos
    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False
    return True

def main():
    word = str(input())
    if palindromo(word):
        print("Es palíndromo")
    else:
        print("No es palíndromo")
if __name__ == "__main__":
    main()
