import numpy as np

# Función para convertir una matriz de números a texto (basado en valores alfabéticos)
def matriz_a_texto(matriz):
    mensaje = ""
    for fila in matriz:
        for num in fila:
            if num == 0:
                mensaje += " "  # Espacio para el valor 0
            elif 1 <= num <= 27:
                mensaje += chr(num + 64)  # Convertir 1 = 'A', 2 = 'B', ..., 26 = 'Z'
            else:
                mensaje += "Z"  # Valores mayores a 26 se consideran como 'Z' (ajuste)
    return mensaje

# Matriz de codificación A
A = np.array([
    [0, 0, 1, -1, 0],
    [0, 4, -1, 1, 2],
    [-2, 4, 1, 1, 2],
    [2, -4, 0, 0, -2],
    [0, 2, -1, 1, 2]
])

# Matriz codificada C
C = np.array([
    [11, 9, -23, 0, 23, 2, -7, 23, -4, 3, -19, 9],
    [111, 35, 135, 122, 115, 72, 113, 121, 56, 33, 99, 43],
    [119, 89, 89, 156, 139, 54, 125, 159, 88, 43, 63, 67],
    [-98, -42, -56, -116, -106, -46, -94, -126, -50, -8, -26, -50],
    [55, 25, 107, 66, 71, 44, 81, 65, 30, 15, 59, 17]
])
print(C.shape,len([11, 9, -23, 0, 23, 2, -7, 23, -4, 3, -19, 9]))
# Determinar si A es invertible y calcular la inversa
if np.linalg.det(A) != 0:
    A_inv = np.linalg.inv(A)
    # Calcular la matriz plana B
    B = np.dot(A_inv, C).round().astype(int)
else:
    B = None

# Convertir la matriz B a texto
mensaje = matriz_a_texto(B)
print(mensaje)
