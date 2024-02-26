#Ordenar en forma acendente la matriz bidimensional
def particionado(fila):
    pivote = fila[0]
    izquierda = []
    derecha = []
    for i in range(1, len(fila)):
        if fila[i] < pivote:
            izquierda.append(fila[i])
        else:
            derecha.append(fila[i])
    return izquierda, pivote, derecha

def quicksort(fila):
    if len(fila) <= 1:
        return fila

    izquierda, pivote, derecha = particionado(fila)
    return quicksort(izquierda) + [pivote] + quicksort(derecha)

# Matriz bidimensional
matriz = [[10, 12, 3],
          [2, 9, 1],
          [5, 4, 6]]

# Ordenar cada fila de la matriz con el metodo  quicksort
matriz_ordenada = [quicksort(fila) for (fila) in matriz]

print("Matriz ordenada acsendente:")
for fila in matriz_ordenada:
    print(fila)
#imprimir la matriz original
matriz_original= matriz
print(("matriz oriinal"))
print(matriz)





