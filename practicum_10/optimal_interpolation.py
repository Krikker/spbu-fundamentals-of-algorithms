from typing import Callable
import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt


def lagrange_basis(i: int, x: float, x_nodes: NDArray):
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    pass


def lagrange_interpolant(x: float, x_nodes: NDArray, y_nodes: NDArray):
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    pass


def plot_data_and_interpolant(x_nodes: NDArray, f: Callable[[float], float]):
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    pass


def runge_func(x: float) -> float:
    return 1.0 / (1 + 25 * x**2)


if __name__ == "__main__":
    # Let's implement optimal Lagrange interpolation and check it
    # on the Runge function

    # Equispaced nodes
    n = 11
    x_equi_nodes = np.linspace(-1.0, 1.0, n)
    plot_data_and_interpolant(x_equi_nodes, runge_func)

    # Optimally located nodes

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################

    x_opt_nodes = None  # should be filled
    plot_data_and_interpolant(x_opt_nodes, runge_func)
