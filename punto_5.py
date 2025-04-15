"""
RETO 1: PUNTO 5
Escribir una función que reciba una lista de string y retorne unicamente
aquellos elementos que tengan los mismos caracteres.
"""
def mismos_caracteres(lista: list) -> list:
    iguales = {}
    #*para cada elemento de la lista, ordena los caracteres y los usa como clave
    for i in lista:
        key = "".join(sorted(i))
        #*si la clave ya existe, agrega el elemento a la lista de valores
        if key in iguales:
            iguales[key].append(i)
        #*si no existe, crea una nueva entrada en el diccionario
        else:
            iguales[key] = [i]
    #*filtra los grupos que tienen más de un elemento
    resultado = [palabra for grupo in iguales.values()
                 if len(grupo) > 1 for palabra in grupo]
    return resultado

def main():
    lista = list(input().split(","))
    resultado = mismos_caracteres(lista)
    print(resultado)

if __name__ == "__main__":
    main() 