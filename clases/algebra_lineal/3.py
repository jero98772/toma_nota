import numpy as np

# Definimos las matrices A, B, y C
A = np.array([[7, -4, 5, 13], [2, -4, 6, 0], [4, 3, 9, 7], [30, -5, 6, 8], [32, 0, 4, 3]])
B = np.array([[-2, 7, 3, 25], [6, 0, -5, 0], [8, 0, -2, -1], [5, -20, 0, 10], [-10, 9, 0, -1]])
C = np.array([[5, -2, -5, 0], [-8, -4, 9, 0], [-3, -4, -5, -2], [0, 5, 5, 0], [-3, 12, 2, 4]])

# Parte a: Resolver 7X - C = 2B - A
# Primero reorganizamos la ecuación: X = (2B - A + C) / 7
X_a = (2 * B - A + C) / 7
print("Parte a: Matriz X que satisface 7X - C = 2B - A")
print(X_a)

# Parte b: Resolver 6B + X = C + 2A + 6X
# Reorganizamos la ecuación: X = (C + 2A - 6B) / 5
X_b = (C + 2 * A - 6 * B) / 5
print("\nParte b: Matriz X que satisface 6B + X = C + 2A + 6X")
print(X_b)
