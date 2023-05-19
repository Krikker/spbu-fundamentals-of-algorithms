class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        pass


if __name__ == "__main__":
    # Let's solve First Missing Positive problem:
    # https://leetcode.com/problems/first-missing-positive
    sol = Solution()
    nums = [0, 1, 2]
    n = sol.firstMissingPositive(nums)
    nums = [2, 1]
    n = sol.firstMissingPositive(nums)
    nums = [1, 2, 0]
    n = sol.firstMissingPositive(nums)
    nums = [3, 4, -1, 1]
    n = sol.firstMissingPositive(nums)
    nums = [7, 8, 9, 11, 12]
    n = sol.firstMissingPositive(nums)
