import numpy as np
import matplotlib.pyplot as plt


def lagrange_basis(i, x, x_nodes):
    x_nodes_except_i = np.r_[x_nodes[:i], x_nodes[i + 1 :]]
    return np.prod((x - x_nodes_except_i) / (x_nodes[i] - x_nodes_except_i))


def lagrange_interpolant(x, x_nodes, y_nodes):
    n = len(x_nodes)
    return np.sum(y_nodes * np.array([lagrange_basis(i, x, x_nodes) for i in range(n)]))


def plot_data_and_interpolant(x_nodes, f):
    y_nodes = f(x_nodes)
    fig, ax = plt.subplots(figsize=(12, 6))
    x_for_plotting = np.linspace(-1, 1, 200)
    ax.plot(x_nodes, y_nodes, "ro", markersize=10)
    ax.plot(x_for_plotting, f(x_for_plotting), "-", color="#aaa", linewidth=4)
    ax.plot(
        x_for_plotting,
        [lagrange_interpolant(x, x_nodes, y_nodes) for x in x_for_plotting],
        "g-",
        linewidth=4,
    )
    ax.grid()
    plt.show()


def runge_func(x: float) -> float:
    return 1.0 / (1 + 25 * x**2)


if __name__ == "__main__":
    # Let's implement optimal Lagrange interpolation and check it
    # on the Runge function
    n = 11
    x_equi_nodes = np.linspace(-1.0, 1.0, n)
    plot_data_and_interpolant(x_equi_nodes, runge_func)

    x_cheby_nodes = np.array(
        [np.cos((2 * i - 1) / (2 * n) * np.pi) for i in range(1, n + 1)]
    )
    plot_data_and_interpolant(x_cheby_nodes, runge_func)
