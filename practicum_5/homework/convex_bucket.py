from time import perf_counter

import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points


def convex_bucket(points: NDArray) -> NDArray:
    """Complexity: O(n log n)"""
    def ccw(p1, p2, p3):
        return (p3[1] - p1[1]) * (p2[0] - p1[0]) > (p2[1] - p1[1]) * (p3[0] - p1[0])

    def dist(p1, p2):
        return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    sorted_index = np.argsort(points[:, 0])
    sorted_points = points[sorted_index]
    p0 = sorted_points[0]
    stack = [p0, sorted_points[1]]

    for i in range(2, len(sorted_points)):
        while len(stack) >= 2 and not ccw(stack[-2], stack[-1], sorted_points[i]):
            stack.pop()
        stack.append(sorted_points[i])
    stack.pop()

    p_max_x = sorted_points[-1]
    if np.array_equal(p0, stack[-1]) and np.array_equal(p_max_x, stack[0]):
        stack_x = np.array(stack)
        p_min_x = stack_x[:, 0].min()
        p_max_x = stack_x[:, 0].max()
        stack = [p for p in stack if p[0] != p_min_x and p[0] != p_max_x]

    stack.insert(0, p0)
    stack.append(p_max_x)
    return np.array(stack + stack[::-1])


if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"points_{i}.txt"
        points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_points(points, convex_hull=ch, markersize=20)
        print()
