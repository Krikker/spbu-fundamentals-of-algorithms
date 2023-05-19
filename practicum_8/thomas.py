import numpy as np
from numpy.typing import NDArray


def thomas(A: NDArray, b: NDArray) -> NDArray:
    """
    Implements Thomas method
    Args:
        A (NDArray): A coef 2D array (N x N) must be tridiagonal matrix
        b (NDArray): b coef 1D array (size=N)
    Returns:
        NDArray: root of the system of linear algebraic equations
    """
    assert A.shape[0] == A.shape[1] and b.shape[0] == A.shape[0]
    A = A.copy()
    b = b.copy()
    gamma = np.zeros(b.shape)
    beta = np.zeros(b.shape)
    root = np.zeros(b.shape)
    N = A.shape[0]
    # fill coefs
    for i in range(0, N - 1):
        gamma[i + 1] = (-A[i][i + 1]) / (A[i][i - 1] * gamma[i] + A[i][i])
        beta[i + 1] = (b[i] - A[i][i - 1] * beta[i]) / (
            A[i][i - 1] * gamma[i] + A[i][i]
        )
    # reverse Thomas
    root[N - 1] = (b[N - 1] - A[N - 1][N - 2] * beta[N - 1]) / (
        A[N - 1][N - 1] + A[N - 1][N - 2] * gamma[N - 1]
    )
    for i in range(N - 1, 0, -1):
        root[i - 1] = gamma[i] * root[i] + beta[i]
    return root


if __name__ == "__main__":
    # Check implementation on simple example
    A = np.array(
        [
            [2, -1, 0, 0, 0],
            [-3, 8, -1, 0, 0],
            [0, -5, 12, 2, 0],
            [0, 0, -6, 18, -4],
            [0, 0, 0, -5, 10],
        ],
        dtype=np.float32,
    )
    b = np.array([-25, 72, -69, -156, 20], dtype=np.float32)
    assert np.all(np.isclose(thomas(A, b), [-10, 5, -2, -10, -3]))
