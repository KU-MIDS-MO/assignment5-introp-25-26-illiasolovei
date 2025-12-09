##task1

# Write a function `column_range_plot(A, filename="column_ranges.pdf")` that;

# - receives a 2D NumPy array `A`,
# - computes the range (maximum minus minimum) of each column,
# - create a bar plot showing the ranges of all columns,
# - saves the plot as a PDF file,
# - and returns a 1D NumPy array containiing the column ranges.

import numpy as np
import matplotlib.pyplot as plt


# Hello Prof. Ramezani
# I left an ipynb file for you in this directory
# I experienced problems starting the plotting subprogram from my terminal so if you
# have them too feel free to use the file from jupyter or spyder
def get_column_min_max(col):
    min = max = col[0]
    for i in range(0, col.shape[0]):
        if col[i] < min:
            min = col[i]
        elif max < col[i]:
            max = col[i]
    return max - min


def column_range_plot(A, filename="column_ranges.pdf"):
    cols = A.shape[1]
    collection = []
    rg = range(0, cols)
    for x in rg:
        current = A[:, x]
        min_max_range = get_column_min_max(current)
        collection.append(min_max_range)
    x_axis = np.arange(cols)
    plt.bar(x_axis, collection)
    plt.xticks(rg, ["Col I", "Col II", "Col III"])
    plt.title("Ranges")
    plt.ylabel("Range value (max - min)")
    plt.xlabel("Column index")

    plt.savefig(filename, format="pdf")
    plt.plot()
    return collection
