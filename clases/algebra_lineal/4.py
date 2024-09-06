import numpy as np

# Definir las masas y los puntos
m1, m2, m3, m4 = 4, 2, 3, 5
v1 = np.array([2, -2, 4])
v2 = np.array([-4, 2, 3])
v3 = np.array([4, 0, -2])
v4 = np.array([1, -6, 0])

# Calcular la masa total
m_total = m1 + m2 + m3 + m4

# Calcular el centro de gravedad
v_cg = (m1 * v1 + m2 * v2 + m3 * v3 + m4 * v4) / m_total

print("Parte a: Centro de gravedad del sistema:", v_cg)
# Puntos de los vértices
v1_b = np.array([1, 1, 1])
v2_b = np.array([8, 1, 0])
v3_b = np.array([2, 4, 3])

# Masas del sistema conocido
m1_known, m2_known, m3_known = 2, 1, 6
m_total_known = m1_known + m2_known + m3_known

# Calcular el centro de masa del sistema conocido
v_known = (m1_known * v1_b + m2_known * v2_b + m3_known * v3_b) / m_total_known

print("Centro de gravedad del sistema conocido:", v_known)

# Ahora planteamos el sistema de ecuaciones para el sistema original
# Sabemos que: m1 * v1 + m2 * v2 + m3 * v3 = m_total * v_known
A = np.array([v1_b, v2_b, v3_b]).T  # Matriz de los puntos
b = m_total_known * v_known          # Vector del sistema conocido

# Resolver el sistema de ecuaciones lineales para m1, m2, m3
m_values = np.linalg.solve(A, b)
print("Parte b: Valores de m1, m2, m3:", m_values)
