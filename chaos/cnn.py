from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def cnn(state, t):
    x1, x2, x3, x4, x5, x6 = state
    result = np.array([-x3 - x4,
                       2 * x2 + x3,
                       12 * x1 - 13 * x2,
                       95 * x1 - 100 * x4 + 200 * f(x4),
                       x1 + 18 * x2 - x5,
                       100 * x2 + 4 * x5 - 4 * x6])
    return result


def f(x):
    return 0.5 * (abs(x + 1) - abs(x - 1))


if __name__ == '__main__':
    s0 = (0.2, 0.2, 0.2, 0.2, 0.2, 0.2)
    t = np.arange(0, 300, 0.01)
    s = odeint(cnn, s0, t)
    print(s)
    plt.figure(figsize=(9, 6), facecolor='w')
    ax = plt.subplot(121, projection='3d')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')
    plt.plot(s[:, 2], s[:, 3], s[:, 4], c='g', lw=1)
    plt.title('cnn', fontsize=16)
    plt.show()
