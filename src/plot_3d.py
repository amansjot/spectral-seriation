# plot a 3d function in the form z = w(x, y)

from matplotlib import pyplot as plt
import numpy as np

def plot_3D(func: callable, num_points: int):
    x = np.linspace(0, 1, num_points)
    y = np.linspace(0, 1, num_points)

    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)

    for i in range(num_points):
        for j in range(num_points):
            Z[i][j] = func(X[i][j], Y[i][j])

    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.plot_surface(X, Y, Z)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

if __name__ == '__main__':
    h = lambda x, y: max(min(x, 1 - x), min(y, 1 - y))
    w = lambda x, y: 1 - h(x, y) if np.sign(x - 1/2) == np.sign(y - 1/2) else h(x, y)
    
    plot_3D(w, 101)