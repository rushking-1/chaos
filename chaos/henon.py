import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def henon(state, t):
    a, b = state
    x1 = [1]
    x2 = [1]
    x3 = [1]
    x4 = [1]
    x5 = [1]
    for k in range(t):
        x1.insert(k + 1, a - (x4[k]) ** 2 - b * x5[k])
        x2.insert(k + 1, x1[k])
        x3.insert(k + 1, x2[k])
        x4.insert(k + 1, x3[k])
        x5.insert(k + 1, x4[k])
    result = np.array([x1, x2, x3, x4, x5])
    result = result.T
    return result


if __name__ == '__main__':
    state = 1.76, 0.1
    t = 400
    s = henon(state, t)
    print(s)
    plt.figure(figsize=(9, 6), facecolor='w')
    ax = plt.subplot(121, projection='3d')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')
    plt.plot(s[:, 0], s[:, 1], s[:, 2], c='g', lw=1)
    plt.title('henon', fontsize=16)
    plt.show()
