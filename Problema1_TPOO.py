#Cree un proyecto en Python donde cree un arreglo de int de un tamaño indicado por el usuario y se llene con números aleatorios de entre 2 a 4 cifras. Cree una función recursiva que indique el promedio entre el máximo y mínimo valor del arreglo tal que sean múltiplos de 3.

import random

def buscar_multiplos_de_3(lista, indice, maximo, minimo):
    if indice >= len(lista):
        return (maximo + minimo) / 2 if maximo != float('-inf') and minimo != float('inf') else None
    
    numero = lista[indice]
    
    if numero % 3 == 0:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
            
    return buscar_multiplos_de_3(lista, indice + 1, maximo, minimo)
def main():
    tamaño = int(input("Ingrese el tamaño del arreglo: "))
    arreglo = [random.randint(10, 999) for _ in range(tamaño)]
    
    print("Arreglo generado:", arreglo)
    resultado = buscar_multiplos_de_3(arreglo, 0, float('-inf'), float('inf'))
    print("El promedio entre el máximo y mínimo valor múltiplo de 3 es:", resultado)
if __name__ == "__main__":    main()

    
