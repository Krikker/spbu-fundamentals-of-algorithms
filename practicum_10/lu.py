import numpy as np
from numpy.typing import NDArray

def lu(A: NDArray, permute: bool) -> tuple[NDArray, NDArray, NDArray]:
    n = A.shape[0]
    L = np.eye(n)
    U = np.copy(A)
    P = np.eye(n)

    for k in range(n - 1):
        if permute:
            # Partial pivoting
            max_row = np.argmax(np.abs(U[k:, k])) + k
            if max_row != k:
                # Swap rows in U
                U[[k, max_row], :] = U[[max_row, k], :]
                # Swap rows in P
                P[[k, max_row], :] = P[[max_row, k], :]
                # Swap rows in L (from k=1 to n-1)
                if k >= 1:
                    L[[k, max_row], :k] = L[[max_row, k], :k]

        for j in range(k + 1, n):
            L[j, k] = U[j, k] / U[k, k]
            U[j, k:] -= L[j, k] * U[k, k:]

    return L, U, P

def solve(L: NDArray, U: NDArray, P: NDArray, b: NDArray) -> NDArray:
    n = L.shape[0]
    y = np.zeros(n)

    # Forward substitution: Ly = Pb
    for i in range(n):
        y[i] = b[np.argmax(P[i])] - np.dot(L[i, :i], y[:i])

    x = np.zeros(n)

    # Back substitution: Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x


def get_A_b(a_11: float, b_1: float) -> tuple[NDArray, NDArray]:
    A = np.array([[a_11, 1.0, -3.0], [6.0, 2.0, 5.0], [1.0, 4.0, -3.0]])
    b = np.array([b_1, 12.0, -39.0])
    return A, b


if __name__ == "__main__":
    # Let's implement the LU decomposition with and without pivoting
    # and check its stability depending on the matrix elements
    p = 9  # modify from 7 to 16 to check instability
    a_11 = 3 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    b_1 = -16 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    A, b = get_A_b(a_11, b_1)
    # With pivoting
    L, U, P = lu(A, permute=True)
    x = solve(L, U, P, b)
    assert np.allclose(x, [1, -7, 4], atol=1e-6), f"The answer {x} is not accurate enough"
    # Without pivoting
    L, U, P = lu(A, permute=False)
    x_ = solve(L, U, P, b)
    assert np.allclose(x_, [1, -7, 4], atol=1e-6), f"The answer {x_} is not accurate enough"


