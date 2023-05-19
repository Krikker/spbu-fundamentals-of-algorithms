import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt


def qubic_spline_coeff(x_nodes: NDArray, y_nodes: NDArray) -> NDArray:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    pass


def qubic_spline(x: float, x_nodes: NDArray, qs_coeff: NDArray) -> float:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    pass


if __name__ == "__main__":
    # Let's build a cubic spline and use it to interpolate GRP

    gdp = np.array(
        [
            506500154001.466,
            516814258695.568,
            517962962962.963,
            460290556900.726,
            435083713850.837,
            395077301248.464,
            395531066563.296,
            391719993756.828,
            404926534140.017,
            270953116950.026,
            195905767668.562,
            259708496267.33,
            306602673980.117,
            345110438692.185,
            430347770731.787,
            591016690742.798,
            764017107992.391,
            989930542278.695,
            1299705247685.76,
            1660844408499.61,
            1222643696991.85,
            1524916112078.87,
            2031768558635.85,
            2170143623037.67,
            2230625004653.55,
            2063662281005.13,
            1365865245098.18,
            1283162348132.8,
        ]
    )
    years = np.arange(1989.0, 2017.0)
    x = np.linspace(years[0], years[-1], 500)
    coeff = qubic_spline_coeff(years, gdp)
    spline_vectorized = np.vectorize(qubic_spline, excluded=set((1, 2)))
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.plot(years, gdp, "x", markersize=10)
    ax.plot(x, spline_vectorized(x, years, coeff))
    ax.grid()
    plt.show()
