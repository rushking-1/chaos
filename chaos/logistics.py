import numpy as np
import matplotlib.pyplot as plt


def logistics(x0, start):
    chaos_seq = []
    for i in range(start):
        x = 3.6 * x0 * (1 - x0)
        x0 = x
        chaos_seq.append(x)
    result = np.array(chaos_seq)
    return result


if __name__ == '__main__':
    x0 = 0.1
    result = logistics(x0, start=500)
    x = range(len(result))
    print(result)
    plt.title('logistics', fontsize=16)
    plt.plot(result)
    plt.show()
