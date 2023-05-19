import numpy as np


def randomized_partition(A, p, r):
    i = np.random.randint(low=p, high=r + 1)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def partition(A, p, r):
    """Rearrange the subarray A[p, ..., r] in place
    It always selected an element x = A[r] as a pivot
    element around which to partition the subarray
    A[p, ..., r]
    """
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def randomized_select(A, p, r, i):
    """Return the ith smallest element of the array A[p, ..., r]"""
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:  # the pivot value is the answer
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)


if __name__ == "__main__":
    # Let's implement a randomized algorithm for finding the median.
    # It has expected linear time
    A = np.random.randint(100, size=10)
    i = 3
    q = randomized_select(A, p=0, r=len(A) - 1, i=i)
    A.sort()
    assert A[i - 1] == q, "Something is wrong!"
    print()
#    for i in range(1, len(commands)):
#        command = commands[i]
#        arg_list = args[i]
#        if command == "put":
#            returned_values.append(lru_cache.put(*arg_list))
#        if command == "get":
#            returned_values.append(lru_cache.get(*arg_list))
#    assert returned_values == [None, None, None, 1, None, -1, None, -1, 3, 4]
