##task2

# Write a function `detect_turning_points(signal, filename="turning_points.pdf")` that:

# - receives a 1D NumPy array representing a signal
# - identifies all indices where the direction of the signal changes
#   (i.e., where the discrete difference changes sign),
# - plots the signal and mark these turning points,
# - saves the figure as a PDF file,
# - and returns a NumPy array containing the indices of the detected points

import numpy as np
import matplotlib.pyplot as plt


def get_signs(collection):
    signs = []
    for i, x in enumerate(collection):
        if i == len(collection) - 1:
            continue
        diff = collection[i + 1] - x
        if diff < 0:
            signs.append(-1)
        elif diff == 0:
            signs.append(0)
        else:
            signs.append(1)
    return np.array(signs)


def detect_turning_points(signal, filename="turning_points.pdf"):
    signs = get_signs(signal)

    prod = signs[1:] * signs[:-1]
    mask = prod < 0
    turned_ids = np.nonzero(mask)[0] + 1

    x_axis = np.arange(signal.size)
    plt.plot(x_axis, signal, marker="o")
    plt.scatter(turned_ids, signal[turned_ids], s=60)
    plt.xlabel("Index")
    plt.ylabel("Signal")
    plt.title("Signal and its turning points")
    plt.savefig(filename)
    plt.close()

    return turned_ids
