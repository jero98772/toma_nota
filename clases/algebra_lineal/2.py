import numpy as np
import matplotlib.pyplot as plt

# Definir los vectores
u = np.array([-45, 3])
v = np.array([-5, -5])
p = np.array([-4.64, 0.31])
h = v - p

# Graficar los vectores p, h, y v
plt.figure(figsize=(8, 8))

# Origen de los vectores
origin = np.array([0, 0])

# Graficar los vectores
plt.quiver(*origin, *v, color='r', scale=1, scale_units='xy', angles='xy', label='v (rojo)')
plt.quiver(*origin, *p, color='g', scale=1, scale_units='xy', angles='xy', label='p (verde)')
plt.quiver(*p, *h, color='b', scale=1, scale_units='xy', angles='xy', label='h (azul)')

# Añadir etiquetas y leyenda
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

plt.title('Gráfico de los vectores p, h y v')
plt.show()

# Parte c
# Definir la matriz A
A = np.array([[-1, 0], [0, -1]])

# Calcular el vector z = A * u
z = A.dot(u)

# Graficar los vectores u y z
plt.figure(figsize=(8, 8))

# Graficar los vectores
plt.quiver(*origin, *u, color='purple', scale=1, scale_units='xy', angles='xy', label='u (morado)')
plt.quiver(*origin, *z, color='orange', scale=1, scale_units='xy', angles='xy', label='z (naranja)')

# Añadir etiquetas y leyenda
plt.xlim(-50, 50)
plt.ylim(-50, 50)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

plt.title('Gráfico de los vectores u y z')
plt.show()
