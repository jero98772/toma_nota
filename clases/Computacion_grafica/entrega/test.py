import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def cubic_bezier(p0, p1, p2, p3, t):
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3

# Control points in 3D space
p0 = np.array([-100,-100,-1100])
p1 = np.array([-100,100,-1100])
p2 = np.array([-100,100,-900])
p3 = np.array([100,100,-900])
# Calculate points on the Bezier curve
t_values = np.linspace(0, 1, 100)
curve_points = np.array([cubic_bezier(p0, p1, p2, p3, t) for t in t_values])

# Plotting in 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(curve_points[:, 0], curve_points[:, 1], curve_points[:, 2], label='Cubic Bezier Curve', color='blue')
ax.scatter([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], [p0[2], p1[2], p2[2], p3[2]], color='red', label='Control Points')
ax.plot([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], [p0[2], p1[2], p2[2], p3[2]], linestyle='dotted', color='gray')

ax.set_title('Cubic Bezier Curve in 3D')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

plt.show()
