import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # este modulo permite trabajar con modelos 3d es de matplot

def plot_vector3d(ax,vectors3d,z0,**options):
    for v in vectors3d:
        x,y,z = v  #aca asigno cada vector aeso
        # Línea vertical desde z0 hasta z en la posición (x, y)
        ax.plot([x, x], [y, y], [z0, z], color="gray", linestyle='dotted')

        # Línea horizontal desde (0, y, z) hasta (x, y, z)
        ax.plot([0, x], [y, y], [z, z], color="gray", linestyle='dotted')
        
    x_coords, y_coords, z_coords = zip(*vectors3d)
    ax.scatter(x_coords, y_coords, z_coords,**options)
    
a = np.array([3,4,6])
b = np.array([4,7,1])
vector =[]

for i in range(5):
    i= np.array([1,1,1])
    vector.append(i)
    i =  i + 1

vectores = np.array (vector)

all_vectors= [a,b] + list(vectores)

# Creamos un subplot 3D.
fig = plt.figure()
subplot3d = fig.add_subplot(111, projection='3d')

# Establecemos los límites del eje z.
subplot3d.set_zlim([0, 9])

# Graficar todos los vectores 3D.
plot_vector3d(subplot3d, all_vectors, 0, color=["r", "b"] + ["g"] * len(vectores))

# Mostrar el gráfico.
plt.show()
