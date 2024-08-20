# Problema de Suma de Subconjuntos
# --------------------------------
# Dado un conjunto de números enteros no negativos C y un número entero k,
# el objetivo es determinar si existe un subconjunto de C cuya suma sea igual a k.
# Para resolver este problema, se utilizará la técnica de programación dinámica.
#
# La idea es construir una tabla M[i][j] donde:
# - M[i][j] es True si es posible formar la suma j utilizando los primeros i elementos de C.
# - M[i][j] es False en caso contrario.

def subset_sum(conjunto,k):
    n = len(conjunto)
    #  creo la matriz
    M = [[False] * (k + 1) for _ in range(n + 1)]

    # primera columna va en TRUE porque si tengo que sumar 0 con el conjunto vacio ya me basta
    for i in range(n + 1):
        M[i][0] = True
    
    # primera fila (menos el (0,0) va todo en FALSE porque es imposible sumar algo > 0 con 0)
    for i in range(1,k + 1):
        M[0][i] = False

    # completo matriz con progamacion dinamica
    for i in range(1, n + 1):
        for j in range( 1, k + 1):
            if conjunto[i-1] > k:
                 # no puedo incluir el elemento conjunto[i-1] en la suma porq es mas grande que j entonces la fila anterior tambien era FALSE
                M[i][j] = M[i - 1][j]
            else:
                # puedo elegir entre asignar el valor de la posicion de arriba o restar el numero a la columna
                M[i][j] = M[i - 1][j] or M[i - 1][j - conjunto[i - 1]]

    # La solución al problema está en M[n][k]
    return M[n][k]

conjunto = [3, 34, 4, 12, 5, 2]
k = 7
print(subset_sum(conjunto, k))
