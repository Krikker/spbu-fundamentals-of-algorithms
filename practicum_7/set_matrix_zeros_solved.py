class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows_to_zero = set()
        cols_to_zero = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)
        for r in rows_to_zero:
            for j in range(n):
                matrix[r][j] = 0
        for c in cols_to_zero:
            for i in range(m):
                matrix[i][c] = 0


if __name__ == "__main__":
    # Let's solve Set Matrix Zeros:
    # https://leetcode.com/problems/set-matrix-zeroes/
    sol = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
