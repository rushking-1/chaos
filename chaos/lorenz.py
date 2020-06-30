from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz(state, t):
    sigma = 10
    rho = 30
    beta = 3
    x, y, z = state
    result = np.array([sigma * (y - x), x * rho - y - x * z, x * y - beta * z])
    return result


if __name__ == '__main__':
    s0 = (0., 1., 0.)
    t = np.arange(0, 200, 0.01)
    s = odeint(lorenz, s0, t)
    print(s)
    plt.figure(figsize=(9, 6), facecolor='w')
    ax = plt.subplot(121, projection='3d')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')
    plt.plot(s[:, 0], s[:, 1], s[:, 2], c='g', lw=1)
    plt.title('lorenz', fontsize=16)
    plt.show()
