import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points


def isclose(p: NDArray, q: NDArray) -> bool:
    return np.isclose(p, q).all()


def signed_area(p: NDArray, q: NDArray, r: NDArray) -> bool:
    signed_area = np.linalg.det(
        np.array(
            [
                np.concatenate((p, [1])),
                np.concatenate((q, [1])),
                np.concatenate((r, [1])),
            ]
        )
    )
    # if np.abs(signed_area) < 0.1:
    #    print(int(np.rint(signed_area)))
    return int(
        np.rint(signed_area)
    )  # check what happens if we use "return signed_area" instead!


def slow_convex_hull(points: NDArray) -> NDArray:
    ch = {}  # key is input point, value is output point; to avoid sorting
    for p in points:  # greedy thru all the points
        for q in points:  # --//--
            if not isclose(p, q):
                valid = True  # flag to control "no point to the left"
                for r in points:  # greedy thru all the points
                    if (not isclose(r, p)) and (not isclose(r, q)):
                        s = signed_area(p, q, r)
                        if (
                            signed_area(p, q, r) == 0
                        ):  # r is on the same line as p and q
                            pq_dist = np.linalg.norm(p - q)
                            pr_dist = np.linalg.norm(p - r)
                            qr_dist = np.linalg.norm(q - r)
                            if pr_dist + qr_dist <= pq_dist:
                                valid = False
                        elif (
                            signed_area(p, q, r) > 0
                        ):  # r is to the left of p -> q vector
                            valid = False
                if valid:
                    ch[tuple(p)] = tuple(q)

    _, q = ch.popitem()
    clockwise_sorted_ch = [q]  # set of convex hull points sorted clockwise
    while ch:
        next_point = ch.pop(clockwise_sorted_ch[-1])
        clockwise_sorted_ch.append(next_point)
    return np.array(clockwise_sorted_ch)


if __name__ == "__main__":
    points = np.loadtxt("practicum_5/points_1.txt")
    plot_points(points, markersize=20)

    # 1. Slow convex hull. Trivial to implement, but O(N^3)
    print("Slow convex hull")
    print("-" * 32)
    convex_hull = slow_convex_hull(points)
    plot_points(points, convex_hull=convex_hull, markersize=20)
    print()
