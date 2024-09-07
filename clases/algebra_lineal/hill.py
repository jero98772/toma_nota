import numpy as np

# 1. Creamos la matriz de codificación A
A = np.array([
    [0, 0, 1, -1, 0],
    [0, 4, -1, 1, 2],
    [-2, 4, 1, 1, 2],
    [2, -4, 0, 0, -2],
    [0, 2, -1, 1, 2]
])

print("Matriz de codificación A:")
print(A)

# 2. Definimos la matriz codificada C
C = np.array([
    [11, 9, -23, 0, 23, 2, -7, 23, -4, 3, -19, 9],
    [111, 35, 135, 122, 115, 72, 113, 121, 56, 33, 99, 43],
    [119, 89, 89, 156, 139, 54, 125, 159, 88, 43, 63, 67],
    [-98, -42, -56, -116, -106, -46, -94, -126, -50, -8, -26, -50],
    [55, 25, 107, 66, 71, 44, 81, 65, 30, 15, 59, 17]
])

print("\nMatriz codificada C:")
print(C)

# 3. Calculamos la inversa de A
A_inv = np.linalg.inv(A)

# 4. Calculamos la matriz plana B
B = A_inv @ C

print("\nMatriz plana B (antes de la corrección):")
print(B)

# 5. Corregimos los valores de B para que estén entre 1 y 27
B_corregida = np.mod(np.round(B).astype(int), 27)
B_corregida[B_corregida == 0] = 27  # Cambiamos 0 por 27

print("\nMatriz plana B (después de la corrección):")
print(B_corregida)

# 6. Decodificamos el mensaje
alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
mensaje_decodificado = ''.join([alfabeto[num-1] for num in B_corregida.flatten()])

print("\nMensaje decodificado:")
print(mensaje_decodificado)
